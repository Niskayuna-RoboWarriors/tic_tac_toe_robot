import Main

vals=[0,0,0,0,0,0,0]
def servoConfig():
    while True:
        inp=input("ready:")
        if inp.isnumeric():
            serv=int(inp)
            value=float(input("value: "))
            vals[serv]=value
        if inp=='ls':
            print(vals)
        if inp =='s':
            Main.armServo1.set(vals[0])
            Main.armServo2.set(vals[1])
            Main.armServo3.set(vals[2])
            Main.armServo4.set(vals[3])
            Main.armServo5.set(vals[4])
            Main.handServo.set(vals[5])
            Main.baseServo.set(vals[6])