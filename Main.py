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
currentPositions=[armServo1Positions[-1],armServo2Positions[-1],armServo3Positions[-1],armServo4Positions[-1],armServo5Positions[-1]]
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
    moveServos([armServo1Positions[index],armServo2Positions[index],armServo3Positions[index],armServo4Positions[index],armServo5Positions[index]])#move servos to position
    time.sleep(1)
    servos.servo[handServo].angle=90#open the hand
    time.sleep(0.3)
    moveServos([armServo1Positions[-1],armServo2Positions[-1],armServo3Positions[-1],armServo4Positions[-1],armServo5Positions[-1]])#move the servos back
    time.sleep(1)
    baseFrom(baseServoPositions[index])#rotate the base back
    time.sleep(0.5)
    #servos.servo[handServo].angle = 10  # close the hand

def moveServos(newPos):
    steps=100#number of describe steps the servos sold move in
    diffs=[(newPos[0]-currentPositions[0])/steps,(newPos[1]-currentPositions[1])/steps,(newPos[2]-currentPositions[2])/steps,(newPos[3]-currentPositions[3])/steps,(newPos[4]-currentPositions[4])/steps]#the sie of the step each servo needs to take
    for i in range(steps):#move through the steps
        servos.servo[armServo1].angle =currentPositions[0]+diffs[0]*i
        servos.servo[armServo2].angle =currentPositions[1]+diffs[1]*i
        servos.servo[armServo3].angle =currentPositions[2]+diffs[2]*i
        servos.servo[armServo4].angle =currentPositions[3]+diffs[3]*i
        servos.servo[armServo5].angle =currentPositions[4]+diffs[4]*i
        time.sleep(1/steps)#wait an amount of time that makes the hole process take 1 second
    servos.servo[armServo1].angle =newPos[0]#make sure the sermos are at the final position
    servos.servo[armServo2].angle =newPos[1]
    servos.servo[armServo3].angle =newPos[2]
    servos.servo[armServo4].angle =newPos[3]
    servos.servo[armServo5].angle =newPos[4]
    currentPositions[0]=newPos[0]#set the current positions
    currentPositions[1] = newPos[1]
    currentPositions[2] = newPos[2]
    currentPositions[3] = newPos[3]
    currentPositions[4] = newPos[4]

#continous execution stars here
gameRunning=False
print("stating")

while True:#forever
    GUI.updateScreen()
    if gameRunning:#if there is a game happening
        inp = input("enter human player move: ")
        if inp.isnumeric():#if the operator entered a number
            tile=int(inp)#get that as a number
            if 0<= tile <9:#if the number is valid
                if AI.board[tile]==0:#check if the entered tile doesn't have anything on it
                    AI.board[tile]=1#set that tile to be an O
                    if AI.boardFull():#check for a stalemate
                        print("staleMate")
                        gameRunning = False
                        AI.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    if AI.detectWin():#check to see if the player won
                        print("GAME OVER, player won")
                        gameRunning = False
                        AI.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    choice=int(AI.botGo())#have the bot make its choice
                    if choice==-1:#check if the bot returned -1
                        print("staleMate")
                        gameRunning = False
                        AI.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                        continue
                    armMovePos(choice)#have the arm place the robots choice on the board
                    if AI.boardFull():#check for a stalemate
                        print("staleMate")
                        gameRunning = False
                        AI.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    if AI.detectWin():#check if the bot won
                        print("GAME OVER, bot won")
                        gameRunning = False
                        AI.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                else:
                    print("invalid, that already has something on it")
        if inp=="end":#if the entered thing was end
            gameRunning=False
            AI.board=[0,0,0,0,0,0,0,0,0]
        if inp=='c':#if the operator wants to close the claw
            servos.servo[handServo].angle=10
        if inp=='o':#if the operator wants to open the claw
            servos.servo[handServo].angle=90
        if inp=='pb':#if the operator want to print the board to check it
            print(AI.board)

    else:#if not in a game
        inp = input("ready: ")
        if inp=='start':#if the operator want to start a game
            gameRunning = True
            if AI.botGoesFirst:#if the bot is going first have it make its choice
                armMovePos(int(AI.botGo()))
        if inp=='d':#if the operator wants to change the difficulty
            dif=input("enter new difficulty between 0 and 4: ")#get the new difficulty
            if dif.isnumeric():
                if 0<=int(dif)<5:#if the input is valid
                    AI.difficulty=int(dif)
            print("difficulty is now "+str(AI.difficulty))
        if inp=='bf':#if the operator wants to change weather the bot goes first
            AI.botGoesFirst=not AI.botGoesFirst
            print("bot goes first: "+str(AI.botGoesFirst))
        if inp=='c':#if the operator wants to close the claw
            servos.servo[handServo].angle=10
        if inp=='o':# if the operator wants to open the claw
            servos.servo[handServo].angle=90