import Main.GPIO as GPIO#get the instance of GPIO from main


GPIO.setup(23, GPIO.OUT)#initilise the pins as inputs or outputs
GPIO.setup(24, GPIO.IN)

GPIO.output(23, GPIO.HIGH)#write to pins
GPIO.output(23, GPIO.LOW)

GPIO.input(24)#read from pins