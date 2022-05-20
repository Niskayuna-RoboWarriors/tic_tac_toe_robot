import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pins=[23,24,25,8,7,1,22,10,9]
for a in pins:
    GPIO.setup(a, GPIO.IN)

values=[0]
while True:
    values=[-1]
    for a in pins:
        values.append(GPIO.input(a))
    print(values)
    time.sleep(0.1)