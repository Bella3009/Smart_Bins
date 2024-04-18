import smbus
from time import sleep
import cv2
from gpiozero import MotionSensor
from LCD1602 import CharLCD1602

imgPath = "/home/bellagauci/Documents/SmartBin/Image/"

camera = cv2.VideoCapture(0)
pirSensor = MotionSensor(10)
lcd1602 = CharLCD1602()

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

def LCDDisplay(Msg1,Msg2=""):
    lcd1602.init_lcd()
    
    lcd1602.clear()
    lcd1602.write(0,0,Msg1)
    lcd1602.write(0,1,Msg2)

def noPIRMotion():
    print("No motion detected")
    sleep(1)
    
def motionPIRDetected():
    print("Motion detected")
    LCDDisplay("Welcome","Show Image")
    sleep(2)
    
    captureImage()
    sleep(1.5)
    LCDDisplay("Item Detected")
    
    
def PIRLoop():
    while True:
        if pirSensor.value == 1:
            motionPIRDetected()
            sleep(5)
        else:
            noPIRMotion()

if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        PIRLoop()
    except KeyboardInterrupt:
        print("Ending program")
        LCDDisplay("Ending program")
        lcd1602.clear()
