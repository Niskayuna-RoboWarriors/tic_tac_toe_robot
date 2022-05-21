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
    print("chose: "+str(index))
    baseTo(baseServoPositions[index])#rotate the base to the position
    servos.servo[armServo1].angle = armServo1Positions[index]#move the servos to posiution
    servos.servo[armServo2].angle = armServo2Positions[index]
    servos.servo[armServo3].angle = armServo3Positions[index]
    servos.servo[armServo4].angle = armServo4Positions[index]
    servos.servo[armServo5].angle = armServo5Positions[index]
    time.sleep(2)
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
    #servos.servo[handServo].angle = 10  # close the hand


#continous execution stars here
gameRunning=False
print("statring")
#servoConfigTest.servoConfig(servos,armServo1,armServo2,armServo3,armServo4,armServo5,handServo)
while True:#forever
    GUI.updateScreen()
    if gameRunning:
        inp = input("enter human player move")
        if inp.isnumeric():
            tile=int(inp)
            if 0<= tile <9:
                if AI.board[tile]==0:
                    AI.board[tile]=1
                    armMovePos(int(AI.botGo()))
                    if AI.boardFull():
                        print("staleMate")
                        gameRunning = False
                        AI.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    if AI.detectWin():
                        print("GAME OVER")
                        gameRunning = False
                        AI.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                else:
                    print("invalid, that already has something on it")
        if inp=="end":
            gameRunning=False
            AI.board=[0,0,0,0,0,0,0,0,0]
        if inp=='c':
            servos.servo[handServo].angle=10
        if inp=='o':
            servos.servo[handServo].angle=10
        if inp=='pb':
            print(AI.board)

    else:
        inp = input("ready: ")
        if inp=='start':
            gameRunning = True
            if AI.botGoesFirst:
                armMovePos(int(AI.botGo()))
        if inp=='d':
            dif=input("enter new difficulty between 0 and 4: ")
            if dif.isnumeric():
                if 0<=int(dif)<5:
                    AI.difficulty=int(dif)
            print("difficulty is now "+str(AI.difficulty))
        if inp=='bf':
            AI.botGoesFirst=not AI.botGoesFirst
            print("bot goes first: "+str(AI.botGoesFirst))
        if inp=='c':
            servos.servo[handServo].angle=10
        if inp=='o':
            servos.servo[handServo].angle=90