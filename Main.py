#this is the main file to run at the start of the program
#import RPi.GPIO as GPIO #this will be used on the actual device
import gpio as GPIO# fake raspberry PI io library for development on not raspberry pi comment this out for any test/builds on a real PI
import ServoController
import AI
import time
GPIO.setmode(GPIO.BCM)#set the pin numbering mode
#numbers of the pins the servos are connected to
armServo1Pin=1#theese need to be set
armServo2Pin=1
armServo3Pin=1
armServo4Pin=1
armServo5Pin=1
handServoPin=1
baseServoPin=1
#configure the pins
GPIO.setUp(armServo1Pin,GPIO.output)
GPIO.setUp(armServo2Pin,GPIO.output)
GPIO.setUp(armServo3Pin,GPIO.output)
GPIO.setUp(armServo4Pin,GPIO.output)
GPIO.setUp(armServo5Pin,GPIO.output)
GPIO.setUp(handServoPin,GPIO.output)
GPIO.setUp(baseServoPin,GPIO.output)
#initilise the servo controllers
armServo1=ServoController.Servo(armServo1Pin)
armServo2=ServoController.Servo(armServo2Pin)
armServo3=ServoController.Servo(armServo3Pin)
armServo4=ServoController.Servo(armServo4Pin)
armServo5=ServoController.Servo(armServo5Pin)
handServo=ServoController.Servo(handServoPin)
baseServo=ServoController.Servo(baseServoPin)
#servo positions for each tile
armServo1Positions=[0,0,0,0,0,0,0,0,0]#theese need to be set
armServo2Positions=[0,0,0,0,0,0,0,0,0]
armServo3Positions=[0,0,0,0,0,0,0,0,0]
armServo4Positions=[0,0,0,0,0,0,0,0,0]
armServo5Positions=[0,0,0,0,0,0,0,0,0]
baseServoPositions=[0,0,0,0,0,0,0,0,0]
#configure buttons and LED pins
goButtonPin=1
difficultyButtonPin=1
GPIO.setUp(goButtonPin,GPIO.input)
GPIO.setUp(difficultyButtonPin,GPIO.input)
redPin=1
greenPin=1
bluePin=1
GPIO.setUp(redPin,GPIO.output)
GPIO.setUp(greenPin,GPIO.output)
GPIO.setUp(bluePin,GPIO.output)

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

#continous execution stars here
setLED()
while True:#forever
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
        armServo1.set(armServo1Positions[tile])#move the arm to that position
        armServo2.set(armServo2Positions[tile])
        armServo3.set(armServo3Positions[tile])
        armServo4.set(armServo4Positions[tile])
        armServo5.set(armServo5Positions[tile])
        baseServo.set(baseServoPositions[tile])
        time.sleep(0.5)#give the arm time to move there
        handServo.set(0)#open the hand
        time.sleep(0.25)#give it time
        armServo1.set(0)#reset the arm back to initial positions
        armServo2.set(0)
        armServo3.set(0)
        armServo4.set(0)
        armServo5.set(0)
        baseServo.set(0.5)
        time.sleep(0.5)#give the arm time to move
        handServo.set(1)#close the hand grabbing the next O
        time.sleep(0.25)#give it time