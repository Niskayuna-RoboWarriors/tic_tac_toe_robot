import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
baseServoSleepPin=14
baseServoDirectionPin=15
baseServoStepPin=18
GPIO.setup(baseServoSleepPin, GPIO.OUT)#configure pins
GPIO.setup(baseServoDirectionPin,GPIO.OUT)
GPIO.setup(baseServoStepPin,GPIO.OUT)
stepPWM=GPIO.PWM(baseServoStepPin,250)#change the number here to change the frequency in HZ
stepPWM.start(50)#dduty cycle
print("send 'g' to start the motor. 's' to stop the motor. 'f' and then a number to set the frequency. 'd' to change direction")
direction = False
while True:
    inp = input("ready:")
    if inp == 'g':
        GPIO.output(baseServoSleepPin,True)
    if inp == 's':
        GPIO.output(baseServoSleepPin,False)
    if inp == 'f':
        nums=input("frequency:")
        if nums.isnumeric():
            stepPWM.ChangeFrequency(float(nums))
    if inp == 'd':
        GPIO.output(baseServoDirectionPin,not direction)
        direction=not direction