from gpiozero import MotionSensor
from time import sleep

# Setting GPIOs to each sensor
pirSensor = MotionSensor(18)

def noMotion():
    print("No motion detected")
    sleep(1)
    
def motionDetected():
    print("Motion detected")
    sleep(1)
    
def PIRLoop():
    while True:
        if pirSensor.value == 1:
            motionDetected()
        else:
            noMotion()
    
# Starting the program
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        PIRLoop()
    except KeyboardInterrupt:
        print("Ending program")
