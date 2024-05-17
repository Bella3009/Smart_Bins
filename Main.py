from time import sleep
from gpiozero import MotionSensor
import LCDDisplay as display
import Bin1 as b1
import Bin2 as b2
#import Bin3 as b3
import PicDetection as pd

pirSensor = MotionSensor(10)

# Read the values in the text file
with open("Data/Measure1.txt","r") as file:
    reading1 = file.read()

with open("Data/Measure2.txt","r") as file:
    reading2 = file.read()

with open("Data/Measure3.txt","r") as file:
    reading3 = file.read()

def noPIRMotion():
    # This function is only to show that no motion is detected by the PIR
    print("No motion detected")
    sleep(1)
    
def motionPIRDetected():
    '''Once Motion is detected, this function is called which will 
    call the functions one after each other as needed'''
    print("Motion detected")
    sleep(2)
    display.displayMsg("ShowItem","Show item", "to identify it")
    object = pd.itemIdentification() # Take the picture and the recognised item is returned
    sleep(2.5)
    display.displayMsg("ItemDetected","Item Detected")
    sleep(1.5)

    # According to which item is identified the function will be called
    if object == "ToiletPaper":
        b1.servoOpen()
        while True:
            if b1.irSensor.value == 0:
                b1.motionIRDetected()
                break
            else:
                b1.noIRMotion()
        sleep(1.5)
        b1.servoClose()
        b1.distanceMeasure()
    
    elif object == "BananaPeel":
        b2.servoOpen()
        while True:
            if b2.irSensor.value == 0:
                b2.motionIRDetected()
                break
            else:
                b2.noIRMotion()
        sleep(1.5)
        b2.servoClose()
        b2.distanceMeasure()

    '''elif object == "ToothBrush":
        b3.servoOpen()
        while True:
            if b3.irSensor.value == 0:
                b3.motionIRDetected()
                break
            else:
                b3.noIRMotion()
        sleep(1.5)
        b3.servoClose()
        b3.distanceMeasure()'''
        
def PIRLoop():
    '''This function is the start of all the code'''
    display.displayMsg("Welcome","Welcome to","Smart bins")
    sleep(3)
    while True:
        if pirSensor.value == 1:
            print("Motion detected")
            motionPIRDetected()
            sleep(5)
            display.displayMsg("Welcome","Welcome to","Smart bins")
        else:
            noPIRMotion()

if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        b1.servoClose(True) # This is because the first time the program starts the servo goes to position 0 angle while for the project I need it to start at 180
        b2.servoClose(True) # This is because the first time the program starts the servo goes to position 0 angle while for the project I need it to start at 180
        #b3.servoClose(True) # This is because the first time the program starts the servo goes to position 0 angle while for the project I need it to start at 180
        b1.setColor()
        b2.setColor()
        #b3.setColor()
        PIRLoop()
        
    except KeyboardInterrupt:
        print("Ending program")
        # To make sure that when the program is stopped the bins close
        b1.servoClose(True) 
        b2.servoClose(True)
        #b3.servoClose(True)
        b1.led.color = (0, 0, 0)  # off
        b2.led.color = (0, 0, 0)  # off
        #b3.led.color = (0, 0, 0)  # off
        display.displayMsg("Ending","Ending program", "Thank you")
        sleep(3)
        display.lcd1602.clear() # CLear the display of the LCD Display
