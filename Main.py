#this is the main file to run at the start of the program
#import RPi.GPIO as GPIO #this will be used on the actual device
import gpio as GPIO# fake raspberry PI io library for development on not raspberry pi comment this out for any test/builds on a real PI
import ServoController
GPIO.setmode(GPIO.BCM)#set the pin numbering mode
#pin numbers need to be set
armServo1Pin=1
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
armServo1Positions=[0,0,0,0,0,0,0,0,0]
armServo2Positions=[0,0,0,0,0,0,0,0,0]
armServo3Positions=[0,0,0,0,0,0,0,0,0]
armServo4Positions=[0,0,0,0,0,0,0,0,0]
armServo5Positions=[0,0,0,0,0,0,0,0,0]
baseServoPositions=[0,0,0,0,0,0,0,0,0]