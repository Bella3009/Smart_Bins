from time import sleep
from gpiozero import MotionSensor
import LCDDisplay as display
import Bin1 as b1
import Bin2 as b2
import Bin3 as b3
import PicDetection as pd

pirSensor = MotionSensor(10)

def noPIRMotion():
    print("No motion detected")
    sleep(1)
    
def motionPIRDetected():
    print("Motion detected")
    sleep(2)
    display.displayMsg("ShowItem","Show item", "to identify it")
    object = pd.captureImage() # itemIdentification function continues in loop therefore to change at later date once more images are added
    object = 2 # Added just for now to test code until itemIdentification function identifies item properly
    sleep(2.5)
    display.displayMsg("ItemDetected","Item Detected")
    sleep(1.5)

    if object == 1:
        print("Item goes in bin 1")

    elif object == 2:
        print("Item goes in bin 2")

    elif object == 3:
        print("Item goes in bin 3")
        
    '''b1.servoOpen()
    while True:
        if b1.irSensor.value == 0:
            b1.motionIRDetected()
            break
        else:
            b1.noIRMotion()
    sleep(1.5)
    b1.servoClose()
    b1.distanceMeasure()'''
    
def PIRLoop():
    display.displayMsg("Welcome","Welcome to","Smart bins")
    sleep(3)
    while True:
        if pirSensor.value == 1:
            motionPIRDetected()
            sleep(5)
        else:
            noPIRMotion()

if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        b1.servoClose(True) # This is because the first time the program starts the servo goes to position 0 angle while for the project I need it to start at 180
        b2.servoClose(True) # This is because the first time the program starts the servo goes to position 0 angle while for the project I need it to start at 180
        b3.servoClose(True) # This is because the first time the program starts the servo goes to position 0 angle while for the project I need it to start at 180
        b1.distanceMeasure()
        b2.distanceMeasure()
        b3.distanceMeasure()
        PIRLoop()
    except KeyboardInterrupt:
        print("Ending program")
        b1.servoClose(True)
        b2.servoClose(True)
        b3.servoClose(True)
        b1.led.color = (0, 0, 0)  # off
        b2.led.color = (0, 0, 0)  # off
        b3.led.color = (0, 0, 0)  # off
        display.displayMsg("Ending","Ending program", "Thank you")
        sleep(3)
        display.lcd1602.clear()
