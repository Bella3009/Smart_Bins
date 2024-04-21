from time import sleep
import cv2
from gpiozero import MotionSensor
import LCDDisplay as display
import Bin1 as b1

imgPath = "/home/bellagauci/Documents/SmartBin/Image/"

camera = cv2.VideoCapture(0)
pirSensor = MotionSensor(10)

def captureImage():
    print("Capturing image...")
    ret, frame = camera.read()  # Read a frame from the camera
    if ret:
        cv2.imwrite(imgPath+"image.jpg", frame)  # Save the frame as an image
        print("Image captured successfully!")
        image = cv2.imread(imgPath+"image.jpg")
        image = cv2.rotate(image, cv2.ROTATE_180)
        cv2.imwrite(imgPath+"image.jpg", image)
        return True
    else:
        print("Failed to capture image.")
        return False

def noPIRMotion():
    print("No motion detected")
    sleep(1)
    
def motionPIRDetected():
    print("Motion detected")
    sleep(2)
    display.displayMsg("PressButton","Show item", "to identify it")
    captureImage()
    sleep(2.5)
    display.displayMsg("Bin1Open","Item Detected") # Need to change audio file when audio for item detected is done
    sleep(1.5)
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
    
def PIRLoop():
    display.displayMsg("Welcome","Welcome to","Smart bins")
    sleep(3)
    while True:
        if pirSensor.value == 1:
            motionPIRDetected()
            display.displayMsg("PressButton","Show item", "to identify it")
            sleep(5)
        else:
            noPIRMotion()

if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        b1.servoClose(True) # This is because the first time the program starts the servo goes to position 0 angle while for the project I need it to start at 180
        b1.distanceMeasure()
        PIRLoop()
    except KeyboardInterrupt:
        print("Ending program")
        b1.servoClose(True)
        b1.led.color = (0, 0, 0)  # off
        display.displayMsg("Welcome","Ending program") # Audio will be changed later since the Ending program audio is still not done
        sleep(3)
        display.lcd1602.clear()
