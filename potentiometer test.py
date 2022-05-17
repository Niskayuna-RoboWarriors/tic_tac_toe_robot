import RPi.GPIO as GPIO#the library for accessing the IO pins
import time

GPIO.setmode(GPIO.BCM)

pin_a = 20#set the number of pin a
pin_b = 21#set the number of pin b

def discharge():#discharge the capacitor
    GPIO.setup(pin_a, GPIO.IN)#set pin a to input mode
    GPIO.setup(pin_b, GPIO.OUT)#set  pin b to output mode
    GPIO.output(pin_b, False)#set the output of pin b to be low
    time.sleep(0.004)#wait 0.004 seconds

def charge_time():#get the "count" of how long it takes to charge the capacitor
    GPIO.setup(pin_b, GPIO.IN)#set pin b to input mode
    GPIO.setup(pin_a, GPIO.OUT)#set pin a to output mode
    count = 0#reset the counter
    GPIO.output(pin_a, True)#set the output of pin a to be high
    while not GPIO.input(pin_b):#read pin b and while it is low
        count = count + 1#increase the count
    return count

def analog_read():#combine the previous functions
    discharge()#discharge the cap
    return charge_time()#get the charge time

while True:#forever
    print(analog_read())#send the result of charge_tine() to the console
    time.sleep(0.1)#wait 1 second