import AI as ai


def printboard():
    print("=====")
    line = ""
    if ai.board[0] == -1:
        line += "O"
    elif ai.board[0] == 1:
        line += "x"
    else:
        line += " "
    line+=" "
    if ai.board[1] == -1:
        line += "O"
    elif ai.board[1] == 1:
        line += "x"
    else:
        line += " "
    line += " "
    if ai.board[2] == -1:
        line += "O"
    elif ai.board[2] == 1:
        line += "x"
    else:
        line += " "
    line += " "
    print(line)

    line = ""
    if ai.board[3] == -1:
        line += "O"
    elif ai.board[3] == 1:
        line += "x"
    else:
        line += " "
    line += " "
    if ai.board[4] == -1:
        line += "O"
    elif ai.board[4] == 1:
        line += "x"
    else:
        line += " "
    line += " "
    if ai.board[5] == -1:
        line += "O"
    elif ai.board[5] == 1:
        line += "x"
    else:
        line += " "
    line += " "
    print(line)
    line = ""
    if ai.board[6] == -1:
        line += "O"
    elif ai.board[6] == 1:
        line += "x"
    else:
        line += " "
    line += " "
    if ai.board[7] == -1:
        line += "O"
    elif ai.board[7] == 1:
        line += "x"
    else:
        line += " "
    line += " "
    if ai.board[8] == -1:
        line += "O"
    elif ai.board[8] == 1:
        line += "x"
    else:
        line += " "
    line += " "
    print(line)
    print("=====")

ai.difficulty=4
while(True):
    printboard()
    c = int(input("enter cell number"))
    if c==-1:
        continue
    if c==-2:
        print(ai.board)
        continue
    ai.board[c]=1
    ai.botGo()
