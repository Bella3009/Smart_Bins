import smbus
from LCD1602 import CharLCD1602

lcd1602 = CharLCD1602()

def DisplayMsg(Msg1,Msg2=""):
    lcd1602.init_lcd()
    
    lcd1602.clear()
    lcd1602.write(0,0,Msg1)
    lcd1602.write(0,1,Msg2)
    
if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        DisplayMsg("Welcome")
    except KeyboardInterrupt:
        print("Ending program")
        DisplayMsg("Ending program")
        lcd1602.clear()
