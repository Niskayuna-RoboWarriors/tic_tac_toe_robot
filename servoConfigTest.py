

vals=[0,0,0,0,0,0]
def servoConfig(servos,armServo1,armServo2,armServo3,armServo4,armServo5,handServo):
    global vals
    vals=[90,90,90,90,90,90]
    print("send a number between 0 and 5 press enter then send a number for the value to set a servo. or send ls to print current values or send s to apply the values to the servos")
    print("0- wrist servo. 1-last joint before hand. 2- servo under the controller board. 3/4- servos at the base of the arm. 5-claw servo")
    while True:
        inp=input("ready:")
        if inp.isnumeric():
            serv=int(inp)
            value=float(input("value: "))
            vals[serv]=value
        if inp=='ls':
            print(vals)
        if inp =='s':
            servos.servo[armServo1].angle=vals[0]
            servos.servo[armServo2].angle=vals[1]
            servos.servo[armServo3].angle=vals[2]
            servos.servo[armServo4].angle=vals[3]
            servos.servo[armServo5].angle=vals[4]
            servos.servo[handServo].angle=vals[5]