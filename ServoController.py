import threading
import time
import Main.GPIO as GPIO


class Servo:#this class can be used to control a servo but is basically just a PWM controller

    def __init__(this,pinNumber):#constructor
        this.pinNumber = pinNumber#the number of the GPIO pin to use
        this.dutyCycle=0#the % of time the signal spends high
        this.highTime=0#the amount of time (in milliseconds) the pin spends high each cycle
        this.cycleTime=20#number in milliseconds| default frequency is 50HZ(20ms)
        this.lowTime=this.cycleTime#the amount of time(in milliseconds) the pin spends low each cycle
        this.thread=threading.Thread(target=this.run)        #a thread to process the PWM independently of other functions
        this.thread.start()#start the thread

    def set(this,value):#value between 0 and 1 representing the duty-cycle of the signal, position of the servo
        this.highTime=this.cycleTime*value#calculate the high and low times of the singal
        this.lowTime=this.cycleTime-this.highTime
        this.dutyCycle=value

    def setCycleTime(this,millis):#set the cycle time
        this.cycleTime=millis
        this.highTime=this.dutyCycle*millis#re calculate the high and low times
        this.lowTime=millis-this.highTime

    def run(this):#the thread that runs
        while True:
            if this.dutyCycle==0:# if the duty-cycle is 0 the keep the signal low
                GPIO.output(this.pinNumber,GPIO.LOW)
                continue
            if this.dutyCycle==1:#if the duty-cycle is 1 then keep the signal high
                GPIO.output(this.pinNumber,GPIO.HIGH)
                continue
            GPIO.output(this.pinNumber,GPIO.HIGH)#set the pin high for the high part of the cycle
            time.sleep(this.highTime/1000)
            GPIO.output(this.pinNumber,GPIO.LOW)#set the pin low for the remaining time in the cycle
            time.sleep(this.lowTime/1000)