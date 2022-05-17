import RPi.GPIO as GPIO#the library for accessing the IO pins
import time
import analogReader

GPIO.setmode(GPIO.BCM)

pin_a = 20#set the number of pin a
pin_b = 21#set the number of pin b

analog=analogReader.AnalogRead(pin_a,pin_b)

while True:#forever
    print(analog.read())#send the result of charge_tine() to the console
    time.sleep(0.1)#wait 1 second