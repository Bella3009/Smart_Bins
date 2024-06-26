import smbus
from pygame import mixer
from LCD1602 import CharLCD1602
from gpiozero import MotionSensor
from gpiozero import AngularServo
from gpiozero import DigitalInputDevice
from gpiozero import DistanceSensor
from gpiozero import RGBLED
from gpiozero import Button
from signal import pause
from time import sleep

# Setting GPIOs to each sensor
pirSensor = MotionSensor(18)
lcd1602 = CharLCD1602()
irSensor = DigitalInputDevice(12)
button = Button(20)
mixer.init() # Speaker setting

# Setting details for Distance Sensor
trigPin = 27
echoPin = 25
sensor = DistanceSensor(echo=echoPin, trigger=trigPin ,max_distance=3)
binDepth = 23
halfEmpty = 23/2
nearFull = 23/4 # /4 because 4 = 25% meaning that only 25% of the bin is empty

# Setting details for Servo Motor
servoGPIO = 23
SERVO_DELAY_SEC = 0.001 
myCorrection = 0.0
maxPW = (2.5+myCorrection)/1000
minPW = (0.5-myCorrection)/1000
servo = AngularServo(servoGPIO,initial_angle=0,min_angle=0, max_angle=180,min_pulse_width=minPW,max_pulse_width=maxPW)

# Setting details for RGB LED
rLED = 26
gLED = 19
bLED = 13
led = RGBLED(red=rLED, green=gLED, blue=bLED, active_high=True)
    
def LCDDisplay(Msg1,Msg2=""):
    lcd1602.init_lcd()
    
    lcd1602.clear()
    lcd1602.write(0,0,Msg1)
    lcd1602.write(0,1,Msg2)

def servoOpen():
    for angle in range(0, 181, 1):   # make servo rotate from 0 to 180 deg
        servo.angle = angle
        sleep(SERVO_DELAY_SEC)
    sleep(0.5)

def servoClose():
    for angle in range(180, -1, -1): # make servo rotate from 180 to 0 deg
        servo.angle = angle
        sleep(SERVO_DELAY_SEC)
    sleep(0.5)
        
def distanceMeasure():
    distance = sensor.distance * 100
    distance = round(distance, 2)
    return distance
    
def setColor(rDepth):
    if rDepth <= nearFull:
        led.color = (1,0,0)
        LCDDisplay("Bin No is", "nearly full")
        sleep(2)
        LCDDisplay("Press button to","throw next item")
    
    elif rDepth <= halfEmpty and rDepth > nearFull:
        led.color = (1,1,0)
        LCDDisplay("Bin No is", "half full")
        sleep(2)
        LCDDisplay("Press button to","throw next item")
    
    elif rDepth > halfEmpty:
        led.color = (0,1,0)

def info(audioName):
    mixer.music.stop()
    mixer.music.set_volume(1.0)
    mixer.music.load(audioName)
    mixer.music.play()
    while mixer.music.get_busy() == True:
        continue

def motionIRDetected():
    print("Item thrown")
    sleep(1)
    
def noIRMotion():
    print("Item not yet thrown")
    sleep(1)
    
def noPIRMotion():
    print("No motion detected")
    sleep(1)
    
def motionPIRDetected():
    print("Motion detected")
    while True:
        if button.is_pressed:
            print("Waiting for button to be pressed")
            # I don't know why yet but is_pressed is giving True when not pressed.
        else:
            print("Button is pressed, program continue")
            LCDDisplay("Bins No","is opening")
            info("Bin1Open.mp3")
            servoOpen()
            while True:
                if irSensor.value == 0:
                    motionIRDetected()
                    break
                else:
                    noIRMotion()
            LCDDisplay("Bins No","is closing")
            info("Bin1Close.mp3")
            servoClose()
            sleep(4)
            lcd1602.clear()
            distance = distanceMeasure()
            setColor(distance)
            break

def PIRLoop():
    while True:
        if pirSensor.value == 1:
            motionPIRDetected()
        else:
            noPIRMotion()
    
# Starting the program
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        LCDDisplay("Welcome","Press button")
        info("Welcome.mp3")
        sleep(3)
        remainDepth = distanceMeasure()
        setColor(remainDepth)
        sleep(3)
        LCDDisplay("Press button to","throw the item")
        info("PressButton.mp3")
        PIRLoop()
    except KeyboardInterrupt:
        lcd1602.clear()
        servoClose()
        sensor.close()
        LCDDisplay("Ending program")
        sleep(3)
        lcd1602.clear()
        led.color = (0, 0, 0)  # off
