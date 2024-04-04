import smbus
from LCD1602 import CharLCD1602
from gpiozero import MotionSensor
from time import sleep

# Setting GPIOs to each sensor
pirSensor = MotionSensor(18)
lcd1602 = CharLCD1602()

def LCDDisplay(Msg1,Msg2=""):
    lcd1602.init_lcd()
    
    lcd1602.clear()
    lcd1602.write(0,0,Msg1)
    lcd1602.write(0,1,Msg2)
    

def noMotion():
    print("No motion detected")
    sleep(1)
    
    
def motionDetected():
    print("Motion detected")
    LCDDisplay("Welcome","Press button")
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
        lcd1602.clear()
        LCDDisplay("Ending program")
        sleep(5)
        lcd1602.clear()
