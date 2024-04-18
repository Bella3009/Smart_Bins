from time import sleep
from gpiozero import MotionSensor

pirSensor = MotionSensor(10)

def noPIRMotion():
    print("No motion detected")
    sleep(1)
    
def motionPIRDetected():
    print("Motion detected")
    sleep(1)
    
def PIRLoop():
    while True:
        if pirSensor.value == 1:
            motionPIRDetected()
        else:
            noPIRMotion()

if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        PIRLoop()
    except KeyboardInterrupt:
        print("Ending program")
