import Main

vals=[0,0,0,0,0,0,0]
def servoConfig():
    global vals
    vals=[Main.armServo1Positions[-1],Main.armServo2Positions[-1],Main.armServo3Positions[-1],Main.armServo4Positions[-1],Main.armServo5Positions[-1],Main.armServo6Positions[-1],Main.handServoPositions[-1]]
    print("send a number between 0 and 6 press enter then send a number for the value to set a servo. or send ls to print current values or send s to apply the values to the servos")
    while True:
        inp=input("ready:")
        if inp.isnumeric():
            serv=int(inp)
            value=float(input("value: "))
            vals[serv]=value
        if inp=='ls':
            print(vals)
        if inp =='s':
            Main.servos.servo[Main.armServo1].angle=vals[0]
            Main.servos.servo[Main.armServo2].angle=vals[1]
            Main.servos.servo[Main.armServo3].angle=vals[2]
            Main.servos.servo[Main.armServo4].angle=vals[3]
            Main.servos.servo[Main.armServo5].angle=vals[4]
            Main.servos.servo[Main.armServo6].angle=vals[5]
            Main.servos.servo[Main.handServo].angle=vals[6]