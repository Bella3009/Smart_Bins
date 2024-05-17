from time import sleep
from gpiozero import AngularServo
from LCDDisplay import displayMsg
from gpiozero import DigitalInputDevice
from gpiozero import DistanceSensor
from gpiozero import RGBLED

binNo = "2"

irSensor = DigitalInputDevice(24)

# Setting details for Servo Motor
servoGPIO = 15
SERVO_DELAY_SEC = 0.001
myCorrection = 0.0
maxPW = (2.5+myCorrection)/1000
minPW = (0.5-myCorrection)/1000
servo = AngularServo(servoGPIO,initial_angle=0,min_angle=0, max_angle=180,min_pulse_width=minPW,max_pulse_width=maxPW)

# Setting details for Distance Sensor
trigPin = 20
echoPin = 23
sensor = DistanceSensor(echo=echoPin, trigger=trigPin ,max_distance=3)
binDepth = 20
halfEmpty = 23/2
nearFull = 23/4 # /4 because 4 = 25% meaning that only 25% of the bin is empty

# Setting details for RGB LED
rLED = 27
gLED = 9
bLED = 22
led = RGBLED(red=rLED, green=gLED, blue=bLED, active_high=True)

with open("Data/Measure2.txt","r") as file:
    reading2 = file.read()

def servoOpen():
    # For this servo the negative angle makes the most confortable way to open the bin
    displayMsg("Bin2Open","Bin " + binNo + "Open","Bins "+ binNo +"is opening")
    for angle in range(180, -1, -1):   # make servo rotate from 0 to 180 deg therefore open the bin
        servo.angle = angle
        sleep(SERVO_DELAY_SEC)
    sleep(0.5)

def servoClose(endProg=False):
    # this function takes care to signal the servo to close the bin
    if endProg == False: # With this condition, the message will not appear when the program ends or starts
        displayMsg("Bin2Close", "Bin" + binNo + "Close","Bins "+ binNo + "is closing")
    for angle in range(0, 181, 1): # make servo rotate from 180 to 0 deg
        servo.angle = angle
        sleep(SERVO_DELAY_SEC)
    sleep(0.5)

def motionIRDetected():
    print("Item thrown")
    sleep(1)
    
def noIRMotion():
    print("Item not yet thrown")
    sleep(1)

def setColor(rDepth=reading2):
    '''According to the value given as parameter the LED display the color'''
    rDepth= float(rDepth)
    if rDepth <= nearFull:
        led.color = (1,0,0)
        displayMsg("Full","Bin " + binNo +" is", "nearly full")
        sleep(2)
    
    elif rDepth <= halfEmpty and rDepth > nearFull:
        led.color = (1,1,0)
        displayMsg("Half","Bin " + binNo +" is","half full")
        sleep(2)
    
    elif rDepth > halfEmpty:
        led.color = (0,1,0)

def distanceMeasure():
    '''When this function is called the distance sensor measure the distance 
    and the value measured will change the color of the LED if needed
    '''
    distance = sensor.distance * 100
    distance = round(distance, 2)
    print(distance)
    setColor(distance) # Set the color of the LED
    # Save the value in the text file to better retrieve it for the GUI
    with open("Data/Measure2.txt","w") as file:
        file.write(str(distance))
    
if __name__ == "__main__":
    '''setColor(20)
    sleep(2)
    setColor(11)
    sleep(2)
    setColor(2)
    sleep(2)
    led.color = (0, 0, 0)'''
    servoOpen()
    distanceMeasure()
    sleep(2)
    servoClose()
    led.color = (0, 0, 0)  # off