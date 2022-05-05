#this is the main file to run at the start of the program
import RPi.GPIO as GPIO #this will be used on the actual device
#import gpio as GPIO# fake raspberry PI io library for development on not raspberry pi comment this out for any test/builds on a real PI
from gpiozero import Servo
import AI
import time
import analogReader
import GUI
GPIO.setmode(GPIO.BCM)#set the pin numbering mode
#numbers of the pins the servos are connected to
armServo1Pin=1#theese need to be set
armServo2Pin=1
armServo3Pin=1
armServo4Pin=1
armServo5Pin=1
handServoPin=1
baseServoPin=1
baseReader=analogReader.AnalogRead(1,1)
#initilise the servo controllers
armServo1=Servo(armServo1Pin)
armServo2=Servo(armServo2Pin)
armServo3=Servo(armServo3Pin)
armServo4=Servo(armServo4Pin)
armServo5=Servo(armServo5Pin)
handServo=Servo(handServoPin)
baseServo=Servo(baseServoPin)
#servo positions for each tile
#                   1 2 3 4 5 6 7 8 9
armServo1Positions=[0,0,0,0,0,0,0,0,0]#theese need to be set
armServo2Positions=[0,0,0,0,0,0,0,0,0]
armServo3Positions=[0,0,0,0,0,0,0,0,0]
armServo4Positions=[0,0,0,0,0,0,0,0,0]#ser vo values range from -1 to 1
armServo5Positions=[0,0,0,0,0,0,0,0,0]
baseServoPositions=[0,0,0,0,0,0,0,0,0]
initialBasePosition=3
#configure buttons and LED pins
goButtonPin=1
difficultyButtonPin=1
GPIO.setUp(goButtonPin,GPIO.IN)
GPIO.setUp(difficultyButtonPin,GPIO.IN)
redPin=1
greenPin=1
bluePin=1
GPIO.setUp(redPin,GPIO.OUT)
GPIO.setUp(greenPin,GPIO.OUT)
GPIO.setUp(bluePin,GPIO.OUT)

def setLED():#sets the color of the LED based on the current difficulty
    if AI.difficulty == 0:#green
        GPIO.output(redPin, GPIO.LOW)
        GPIO.output(greenPin, GPIO.HIGH)
        GPIO.output(bluePin, GPIO.LOW)
    if AI.difficulty==1:#light blue
        GPIO.output(redPin,GPIO.LOW)
        GPIO.output(greenPin, GPIO.HIGH)
        GPIO.output(bluePin, GPIO.HIGH)
    if AI.difficulty==2:#dark blue
        GPIO.output(redPin,GPIO.LOW)
        GPIO.output(greenPin, GPIO.LOW)
        GPIO.output(bluePin, GPIO.HIGH)
    if AI.difficulty==3:#purpleish white
        GPIO.output(redPin,GPIO.HIGH)
        GPIO.output(greenPin, GPIO.LOW)
        GPIO.output(bluePin, GPIO.HIGH)
    if AI.difficulty==4:#red
        GPIO.output(redPin,GPIO.HIGH)
        GPIO.output(greenPin, GPIO.LOW)
        GPIO.output(bluePin, GPIO.LOW)

def setBasePos(val):
    curVal=baseReader.read()
    while curVal<val-2 or curVal > val:
        if curVal > val:
            baseServo.value=-0.5
        if curVal < val:
            baseServo.value=0.5
        curVal=baseReader.read()

#continous execution stars here
setLED()
GUI.init()
while True:#forever
    GUI.updateScreen()
    if GPIO.input(difficultyButtonPin)==1:#if the difficulty button is pressed
        while GPIO.input(difficultyButtonPin)==1:
            2+2#wait until the button is released
        AI.difficulty+=1#increase the difficulty
        if AI.difficulty==5:#if the difficulty is more than the max then reset it
            AI.difficulty=0
        setLED()#update the LED

    if GPIO.input(goButtonPin)==1:
        #insert CV board updating here
        tile = AI.botGo()#choose where to place the O
        setBasePos(baseServoPositions[tile])#rotate the robot to the correct position
        armServo1.value=armServo1Positions[tile]#move the arm to that position
        armServo2.value=armServo2Positions[tile]
        armServo3.value=armServo3Positions[tile]
        armServo4.value=armServo4Positions[tile]
        armServo5.value=armServo5Positions[tile]
        time.sleep(0.5)#give the arm time to move there
        handServo.value=0#open the hand
        time.sleep(0.25)#give it time
        armServo1.value=0#reset the arm back to initial positions
        armServo2.value=0
        armServo3.value=0
        armServo4.value=0
        armServo5.value=0
        time.sleep(0.5)#give the arm time to move
        setBasePos(initialBasePosition)#move the robot back to it original position
        handServo.value=1#close the hand grabbing the next O
        time.sleep(0.25)#give it time