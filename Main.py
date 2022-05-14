#this is the main file to run at the start of the program
import RPi.GPIO as GPIO #library for interacting with the pins on the pi
import AI
import time
import analogReader
from adafruit_servokit import ServoKit #library for interacting with the servo controller
import GUI
import servoConfigTest
import busio

GUI.init()#start the GUI
GPIO.setmode(GPIO.BCM)#set the pin numbering mode
#numbers of the pins the servos are connected to
baseReader=analogReader.AnalogRead(7,8)
#initilise the servo controller
servos = ServoKit(channels=16,i2c=busio.I2C(3,2))
armServo1=15
armServo2=6
armServo3=5
armServo4=2
armServo5=3
handServo=0
#servo positions for each tile
#                   1  2  3  4  5  6  7  8  9  R
armServo1Positions=[90,90,90,90,90,90,90,90,90,90]#theese need to be set
armServo2Positions=[90,90,90,90,90,90,90,90,90,90]
armServo3Positions=[90,90,90,90,90,90,90,90,90,90]
armServo4Positions=[90,90,90,90,90,90,90,90,90,90]#ser vo values range from -1 to 1
armServo5Positions=[90,90,90,90,90,90,90,90,90,90]
baseServoPositions=[90,90,90,90,90,90,90,90,90,90]
#set servos to their default positions
servos.servo[armServo1].angle=armServo1Positions[-1]
servos.servo[armServo2].angle=armServo2Positions[-1]
servos.servo[armServo3].angle=armServo3Positions[-1]
servos.servo[armServo4].angle=armServo4Positions[-1]
servos.servo[armServo5].angle=armServo5Positions[-1]
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
def setBasePos(val):
    GPIO.output(baseServoSleepPin,True)#start the base motor
    curVal=baseReader.read()
    while curVal<val-2 or curVal > val+2:#set the direction of the motor
        if curVal > val:
            GPIO.output(baseServoDirectionPin,True)
        if curVal < val:
            GPIO.output(baseServoDirectionPin,False)
        curVal=baseReader.read()
    GPIO.output(baseServoSleepPin,False)#stop the base motor

#continous execution stars here

print("statring")
servoConfigTest.servoConfig(servos,armServo1,armServo2,armServo3,armServo4,armServo5,handServo)
while True:#forever
    GUI.updateScreen()
    #if GPIO.input(difficultyButtonPin)==1:#if the difficulty button is pressed
    #    while GPIO.input(difficultyButtonPin)==1:
    #        2+2#wait until the button is released
    #    AI.difficulty+=1#increase the difficulty
    #    if AI.difficulty==5:#if the difficulty is more than the max then reset it
    #        AI.difficulty=0

    if GPIO.input(goButtonPin)==1:
        #insert CV board updating here
        tile = AI.botGo()#choose where to place the O
        setBasePos(baseServoPositions[tile])#rotate the robot to the correct position
        servos.servo[armServo1].angle=armServo1Positions[tile]#move the arm to that position
        servos.servo[armServo2].angle=armServo2Positions[tile]
        servos.servo[armServo3].angle=armServo3Positions[tile]
        servos.servo[armServo4].angle=armServo4Positions[tile]
        servos.servo[armServo5].angle=armServo5Positions[tile]
        time.sleep(0.5)#give the arm time to move there
        servos.servo[handServo]=90#open the hand
        time.sleep(0.25)#give it time
        servos.servo[armServo1].angle=armServo1Positions[-1]#reset the arm back to initial positions
        servos.servo[armServo2].angle=armServo2Positions[-1]
        servos.servo[armServo3].angle=armServo3Positions[-1]
        servos.servo[armServo4].angle=armServo4Positions[-1]
        servos.servo[armServo5].angle=armServo5Positions[-1]
        time.sleep(0.5)#give the arm time to move
        setBasePos(baseServoPositions[-1])#move the robot back to it original position
        servos.servo[handServo]=1#close the hand grabbing the next o
        time.sleep(0.25)#give it time
