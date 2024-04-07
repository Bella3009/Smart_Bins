import smbus
from LCD1602 import CharLCD1602
from gpiozero import MotionSensor
from gpiozero import AngularServo
from gpiozero import DigitalInputDevice
from gpiozero import DistanceSensor
from signal import pause
from time import sleep

# Setting GPIOs to each sensor
pirSensor = MotionSensor(18)
lcd1602 = CharLCD1602()
irSensor = DigitalInputDevice(12)

# Setting details for Distance Sensor
trigPin = 27
echoPin = 25
sensor = DistanceSensor(echo=echoPin, trigger=trigPin ,max_distance=3)

# Setting details for Servo Motor
servoGPIO = 23
SERVO_DELAY_SEC = 0.001 
myCorrection = 0.0
maxPW = (2.5+myCorrection)/1000
minPW = (0.5-myCorrection)/1000
servo = AngularServo(servoGPIO,initial_angle=0,min_angle=0, max_angle=180,min_pulse_width=minPW,max_pulse_width=maxPW)


def LCDDisplay(Msg1,Msg2=""):
    lcd1602.init_lcd()
    
    lcd1602.clear()
    lcd1602.write(0,0,Msg1)
    lcd1602.write(0,1,Msg2)

def servoLoopOpen():
    for angle in range(0, 181, 1):   # make servo rotate from 0 to 180 deg
        servo.angle = angle
        sleep(SERVO_DELAY_SEC)
    sleep(0.5)

def servoLoopClose():
    for angle in range(180, -1, -1): # make servo rotate from 180 to 0 deg
        servo.angle = angle
        sleep(SERVO_DELAY_SEC)
    sleep(0.5)
        
def distanceLoop():
    print('Distance: ', sensor.distance * 100,'cm')
    
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
    LCDDisplay("Bins No","is opening")
    servoLoopOpen()
    while True:
        if irSensor.value == 0:
            motionIRDetected()
            break
        else:
            noIRMotion()
    LCDDisplay("Bins No","is closing")
    servoLoopClose()
    sleep(4)
    lcd1602.clear()
    
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
        sleep(3)
        distanceLoop()
        LCDDisplay("Press button to","throw the next item")
        sleep(3)
        PIRLoop()
    except KeyboardInterrupt:
        lcd1602.clear()
        servoLoopClose()
        sensor.close()
        LCDDisplay("Ending program")
        sleep(3)
        lcd1602.clear()
