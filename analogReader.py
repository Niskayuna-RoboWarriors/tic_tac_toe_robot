import threading
import time
import RPi.GPIO as GPIO

class AnalogRead:

    def __init__(this, pina, pinb):
        this.pin_a=pina
        this.pin_b=pinb
        this.counts=[0]
        #this.thread=threading.Thread(target=this.run)
        #this.thread.start()

    def run(this):
        this.counts.append(this.analog_read())
        if len(this.counts)>30:
            this.counts.pop(0)

    def discharge(this):  # discharge the capacitor
        GPIO.setup(this.pin_a, GPIO.IN)  # set pin a to input mode
        GPIO.setup(this.pin_b, GPIO.OUT)  # set  pin b to output mode
        GPIO.output(this.pin_b, False)  # set the output of pin b to be low
        time.sleep(0.004)  # wait 0.004 seconds

    def charge_time(this):  # get the "count" of how long it takes to charge the capacitor
        GPIO.setup(this.pin_b, GPIO.IN)  # set pin b to input mode
        GPIO.setup(this.pin_a, GPIO.OUT)  # set pin a to output mode
        count = 0  # reset the counter
        GPIO.output(this.pin_a, True)  # set the output of pin a to be high
        while not GPIO.input(this.pin_b):  # read pin b and while it is low
            count = count + 1  # increase the count
        return count

    def analog_read(this):  # combine the previous functions
        this.discharge()  # discharge the cap
        return this.charge_time()  # get the charge time

    def read(this):
        this.run()
        return this.avarage()
    def avarage(this):
        total=0
        for a in this.counts:
            total+=a
        return total/len(this.counts)