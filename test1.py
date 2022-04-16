#import RPi.GPIO as GPIO #this will be used on the actual device
import gpio as GPIO# fake raspberry PI io library for development on not raspberry pi

GPIO.setmode(GPIO.BCM)#set the pin numbering mode

GPIO.setup(23, GPIO.OUT)#initilise the pins as inputs or outputs
GPIO.setup(24, GPIO.IN)

GPIO.output(23, GPIO.HIGH)#write to pins
GPIO.output(23, GPIO.LOW)

GPIO.input(24)#read from pins