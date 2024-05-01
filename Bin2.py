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
trigPin = 23
echoPin = 20
sensor = DistanceSensor(echo=echoPin, trigger=trigPin ,max_distance=3)
binDepth = 20
halfEmpty = binDepth/2
nearFull = binDepth/4  # /4 because 4 = 25% meaning that only 25% of the bin is empty

# Setting details for RGB LED
rLED = 27
gLED = 9
bLED = 22
led = RGBLED(red=rLED, green=gLED, blue=bLED, active_high=True)

def servoOpen():
    # For this servo the negative angle makes the most confortable way to open the bin
    displayMsg("Bin2Open","Bin" + binNo + "Open","Bins "+ binNo,"is opening")
    for angle in range(180, -1, -1):   # make servo rotate from 0 to 180 deg
        servo.angle = angle
        sleep(SERVO_DELAY_SEC)
    sleep(0.5)

def servoClose(endProg=False):
    if endProg == False: # With this condition, the message will not appear when the program ends
        displayMsg("Bin2Close", "Bin" + binNo + "Close","Bins "+ binNo,"is closing")
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

def setColor(rDepth):
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
    distance = sensor.distance * 100
    distance = round(distance, 2)
    print(distance)
    setColor(distance)
    with open("Data/Measure2.txt","w") as file:
        file.write(str(distance))
    
if __name__ == "__main__":
    servoOpen()
    distanceMeasure()
    sleep(2)
    servoClose()
    led.color = (0, 0, 0)  # off
