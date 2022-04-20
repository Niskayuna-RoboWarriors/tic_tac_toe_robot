#this is the main file to run at the start of the program
#import RPi.GPIO as GPIO #this will be used on the actual device
import gpio as GPIO# fake raspberry PI io library for development on not raspberry pi comment this out for any test/builds on a real PI
import ServoController
import AI
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