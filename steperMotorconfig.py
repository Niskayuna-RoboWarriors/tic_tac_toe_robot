import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
baseServoSleepPin=14
baseServoDirectionPin=15
baseServoStepPin=18
GPIO.setup(baseServoSleepPin, GPIO.OUT)#configure pins
GPIO.setup(baseServoDirectionPin,GPIO.OUT)
GPIO.setup(baseServoStepPin,GPIO.OUT)
print("'d' to change direction or a number to make the motor step the number of steps")
direction = False
while True:
    inp = input("ready:")

    if inp == 'd':
        GPIO.output(baseServoDirectionPin,not direction)
        direction=not direction
    if inp.isnumeric():
        GPIO.output(baseServoSleepPin, True)
        for a in range(int(inp)):
            GPIO.output(baseServoStepPin,True)
            time.sleep(0.01)
            GPIO.output(baseServoStepPin,False)
            time.sleep(0.01)
        GPIO.output(baseServoSleepPin,False)