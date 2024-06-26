import smbus
from LCD1602 import CharLCD1602
from pygame import mixer

audioPath = "/home/bellagauci/Documents/SmartBin/Audio/"

lcd1602 = CharLCD1602()
mixer.init() # Speaker setting

def info(audioName):
    # This function starts the audio
    mixer.music.stop()
    mixer.music.set_volume(1.0)
    mixer.music.load(audioPath+audioName+".mp3")
    mixer.music.play()
    while mixer.music.get_busy() == True:
        continue
    
def displayMsg(audio,Msg1,Msg2=""):
    '''Since the display and audio notify the same thing one of the parameters is the audio file.
    The second argument is the first line of the diplay
    The third argument is the second line of the diplay'''
    lcd1602.init_lcd()
    
    lcd1602.clear()
    lcd1602.write(0,0,Msg1)
    lcd1602.write(0,1,Msg2)
    
    info(audio)
    
    
if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        displayMsg("Welcome", "Welcome")
    except KeyboardInterrupt:
        print("Ending program")
        displayMsg("Ending program")
        lcd1602.clear()
