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
            Main.armServo1.value=vals[0]
            Main.armServo2.value=vals[1]
            Main.armServo3.value=vals[2]
            Main.armServo4.value=vals[3]
            Main.armServo5.value=vals[4]
            Main.handServo.value=vals[5]
            Main.baseServo.value=vals[6]