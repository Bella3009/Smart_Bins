from time import sleep
from gpiozero import AngularServo

# Setting details for Servo Motor
servoGPIO = 14
SERVO_DELAY_SEC = 0.001
myCorrection = 0.0
maxPW = (2.5+myCorrection)/1000
minPW = (0.5-myCorrection)/1000
servo = AngularServo(servoGPIO,initial_angle=0,min_angle=0, max_angle=180,min_pulse_width=minPW,max_pulse_width=maxPW)

def servoOpen():
    for angle in range(0, 181, 1):   # make servo rotate from 0 to 180 deg
        servo.angle = angle
        sleep(SERVO_DELAY_SEC)
    sleep(0.5)

def servoClose():
    for angle in range(180, -1, -1): # make servo rotate from 180 to 0 deg
        servo.angle = angle
        sleep(SERVO_DELAY_SEC)
    sleep(0.5)

if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        servoOpen()

    except KeyboardInterrupt:
        servoClose()
