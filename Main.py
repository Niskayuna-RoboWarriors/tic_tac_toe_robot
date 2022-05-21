#this is the main file to run at the start of the program
import RPi.GPIO as GPIO #library for interacting with the pins on the pi
import AI
import time
from adafruit_servokit import ServoKit #library for interacting with the servo controller
import GUI
import servoConfigTest
import busio

GUI.init()#start the GUI
GPIO.setmode(GPIO.BCM)#set the pin numbering mode
#numbers of the pins the servos are connected to
#initilise the servo controller
servos = ServoKit(channels=16,i2c=busio.I2C(3,2))
armServo1=14
armServo2=6
armServo3=5
armServo4=2
armServo5=3
handServo=10
#servo positions for each tile
#                   1  2  3  4  5  6  7  8  9  R
armServo1Positions=[60,60,60,30,30,30,1,1,1,25]#theese need to be set
armServo2Positions=[90,90,90,90,90,90,90,90,90,90]
armServo3Positions=[140,140,140,130,160,160,179,179,179,160]
armServo4Positions=[10,10,10,40,40,40,57,110,75,120]#ser vo values range from -1 to 1
armServo5Positions=[170,170,170,140,140,140,115,80,115,70]
baseServoPositions=[117,100,85,122,100,77,137,100,62,0]
#set servos to their default positions
servos.servo[armServo1].angle=armServo1Positions[-1]
servos.servo[armServo2].angle=armServo2Positions[-1]
servos.servo[armServo3].angle=armServo3Positions[-1]
servos.servo[armServo4].angle=armServo4Positions[-1]
servos.servo[armServo5].angle=armServo5Positions[-1]
servos.servo[handServo].angle=90
#configure the pins for the base servo
baseServoSleepPin=14
baseServoDirectionPin=15
baseServoStepPin=18
GPIO.setup(baseServoSleepPin, GPIO.OUT)#configure pins
GPIO.setup(baseServoDirectionPin,GPIO.OUT)
GPIO.setup(baseServoStepPin,GPIO.OUT)
GPIO.output(baseServoSleepPin,False)
stepPWM=GPIO.PWM(baseServoStepPin,100)#change the number here to change the frequency in HZ
stepPWM.start(50)#start the PWM with a duty cycle of 50
#configure outher buttons
goButtonPin=23
GPIO.setup(goButtonPin,GPIO.OUT)
def baseTo(val):
    print(val)
    GPIO.output(baseServoSleepPin,True)#start the base motor
    GPIO.output(baseServoDirectionPin,False)#set the direction
    for a in range(val):#tell the motor controller to sterp the number of steps
        GPIO.output(baseServoStepPin, True)
        time.sleep(0.01)
        GPIO.output(baseServoStepPin, False)
        time.sleep(0.01)
    GPIO.output(baseServoSleepPin,False)#stop the base motor

def baseFrom(val):
    GPIO.output(baseServoSleepPin,True)#start the base motor
    GPIO.output(baseServoDirectionPin,True)#set the direction
    for a in range(val):#tell the motor controller to sterp the number of steps
        GPIO.output(baseServoStepPin, True)
        time.sleep(0.01)
        GPIO.output(baseServoStepPin, False)
        time.sleep(0.01)
    GPIO.output(baseServoSleepPin,False)#stop the base motor

def armMovePos(index):
    baseTo(baseServoPositions[index])#rotate the base to the position
    servos.servo[armServo1].angle = armServo1Positions[index]#move the servos to posiution
    servos.servo[armServo2].angle = armServo2Positions[index]
    servos.servo[armServo3].angle = armServo3Positions[index]
    servos.servo[armServo4].angle = armServo4Positions[index]
    servos.servo[armServo5].angle = armServo5Positions[index]
    time.sleep(1)
    servos.servo[handServo].angle=90#open the hand
    time.sleep(0.3)
    servos.servo[armServo1].angle = armServo1Positions[-1]#move ther servos back
    servos.servo[armServo2].angle = armServo2Positions[-1]
    servos.servo[armServo3].angle = armServo3Positions[-1]
    servos.servo[armServo4].angle = armServo4Positions[-1]
    servos.servo[armServo5].angle = armServo5Positions[-1]
    time.sleep(1)
    baseFrom(baseServoPositions[index])#rotate the base back
    time.sleep(0.5)
    servos.servo[handServo].angle = 10  # close the hand


#continous execution stars here

print("statring")
#servoConfigTest.servoConfig(servos,armServo1,armServo2,armServo3,armServo4,armServo5,handServo)
while True:#forever
    inp = input("ready:")
    GUI.updateScreen()
    if inp.isnumeric():
        if 0 <= int(inp) < 9:
            armMovePos(int(inp))

        ##insert CV board updating here
        #tile = AI.botGo()#choose where to place the O
        #setBasePos(baseServoPositions[tile])#rotate the robot to the correct position
        #servos.servo[armServo1].angle=armServo1Positions[tile]#move the arm to that position
        #servos.servo[armServo2].angle=armServo2Positions[tile]
        #servos.servo[armServo3].angle=armServo3Positions[tile]
        #servos.servo[armServo4].angle=armServo4Positions[tile]
        #servos.servo[armServo5].angle=armServo5Positions[tile]
        #time.sleep(0.5)#give the arm time to move there
        #servos.servo[handServo]=90#open the hand
        #time.sleep(0.25)#give it time
        #servos.servo[armServo1].angle=armServo1Positions[-1]#reset the arm back to initial positions
        #servos.servo[armServo2].angle=armServo2Positions[-1]
        #servos.servo[armServo3].angle=armServo3Positions[-1]
        #servos.servo[armServo4].angle=armServo4Positions[-1]
        #servos.servo[armServo5].angle=armServo5Positions[-1]
        #time.sleep(0.5)#give the arm time to move
        #setBasePos(baseServoPositions[-1])#move the robot back to it original position
        #servos.servo[handServo]=1#close the hand grabbing the next o
        #time.sleep(0.25)#give it time
