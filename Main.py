#this is the main file to run at the start of the program
#import RPi.GPIO as GPIO #this will be used on the actual device
import gpio as GPIO# fake raspberry PI io library for development on not raspberry pi comment this out for any test/builds on a real PI
GPIO.setmode(GPIO.BCM)#set the pin numbering mode