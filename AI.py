import random
board=[0,0,0,0,0,0,0,0,0]
difficulty=0
botGoesFirst=False

def makeGuess(mode):
    if boardFull():
        return -1
    if detectWin():
        return -1
    if mode==1:
        notPlaced=True
        while notPlaced:
            slot = random.randint(0,8)
            if board[slot]!=0:
                continue
            board[slot]=-1
            notPlaced=False
            return slot
    #end of mode = 1
    if mode==2:
        tmpFalse=False
        if towInaRow()!=-1:#if the player has 2 in a row and can win then win
            board[towInaRow()]=-1
            return towInaRow()
        elif block()!=-1:#Block: If the opponent has two in a row, the player must play the third themselves to block the opponent.
            board[block()]=-1
            return block()
        elif tmpFalse:#Fork: Cause a scenario where the player has two ways to win (two non-blocked lines of 2).
            a=""#i cant be bothered to figure out how to implement these steps
        elif tmpFalse:#Blocking an opponent's fork: If there is only one possible fork for the opponent, the player should block it. Otherwise, the player should block all forks in any way that simultaneously allows them to make two in a row. Otherwise, the player should make a two in a row to force the opponent into defending, as long as it does not result in them producing a fork. For example, if "X" has two opposite corners and "O" has the center, "O" must not play a corner move to win. (Playing a corner move in this scenario produces a fork for "X" to win.)
            a=""
        elif board[4]==0:#Center: A player marks the center.
            board[4]=-1
            return 4
        elif opposetCorner()!=-1:#Opposite corner: If the opponent is in the corner, the player plays the opposite corner.
            board[opposetCorner()]=-1
            return opposetCorner()
        elif emptyCorner():#Empty corner: The player plays in a corner square.
            board[emptyCorner()]=-1
            return emptyCorner()
        elif emptySide()!=-1:#Empty side: The player plays in a middle square on any of the four sides.
            board[emptySide()]=-1
            return emptySide()
        else:#if somehow it didn't decide to do one of the previous then randomly choose a place to place
            return makeGuess(1)
    #end of mode 2

def botGo():#call this function to have the bot make its move
    randMode=random.randint(0,100)
    if difficulty==0:
        return makeGuess(1)
    if difficulty==1:
        if randMode>75:
            return makeGuess(2)
        else:
            return makeGuess(1)
    if difficulty==2:
        if randMode>50:
            return makeGuess(2)
        else:
            return makeGuess(1)
    if difficulty==3:
        if randMode>25:
            return makeGuess(2)
        else:
            return makeGuess(1)
    if difficulty==4:
        return makeGuess(2)



def boardFull():
    return board[0] != 0 and board[1] != 0 and board[2] != 0 and board[3] != 0 and board[4] != 0 and board[5] != 0 and board[6] != 0 and board[7] != 0 and board[8] != 0

def detectWin():
    i =-1
    for a in range (2): # check for both O and X
        if board[0] == i and board[1] == i and board[2] == i:# top row
            return True

        if board[3] == i and board[4] == i and board[5] == i:# middle row
            return True

        if board[6] == i and board[7] == i and board[8] == i:# bottom row
            return True

        if board[0] == i and board[3] == i and board[6] == i:# left colom
            return True

        if board[1] == i and board[4] == i and board[7] == i:# middle colom
            return True

        if board[2] == i and board[5] == i and board[8] == i:# right colom
            return True

        if board[0] == i and board[4] == i and board[8] == i:# diagonal 1
            return True

        if board[2] == i and board[4] == i and board[6] == i:# diagonal 2
            return True

    return False

def towInaRow():
    #top row
    if board[0] == -1 and board[1] == -1 and board[2] == 0:
        return 2
    if board[0] == -1 and board[1] == 0 and board[2] == -1:
        return 1
    if board[0] == 0 and board[1] == -1 and board[2] == -1:
        return 0
    #middle row
    if board[3]==-1 and board[4]==-1 and board[5]==0:
        return 5
    if board[3]==-1 and board[4]==0 and board[5]==-1:
        return 4
    if board[3]==0 and board[4]==-1 and board[5]==-1:
        return 3
    #bottom row
    if board[6]==-1 and board[7]==-1 and board[8]==0:
        return 8
    if board[6]==-1 and board[7]==0 and board[8]==-1:
        return 7
    if board[6]==0 and board[7]==-1 and board[8]==-1:
        return 6
    #verticle
    #left colom
    if board[0]==-1 and board[3]==-1 and board[6]==0:
        return 6
    if board[0]==-1 and board[3]==0 and board[6]==-1:
        return 3
    if board[0]==0 and board[3]==-1 and board[6]==-1:
        return 0
    #middle colom
    if board[1]==-1 and board[4]==-1 and board[7]==0:
        return 7
    if board[1]==-1 and board[4]==0 and board[7]==-1:
        return 4
    if board[1]==0 and board[4]==-1 and board[7]==-1:
        return 1
    #right colom
    if board[2]==-1 and board[5]==-1 and board[8]==0:
        return 8
    if board[2]==-1 and board[5]==0 and board[8]==-1:
        return 5
    if board[2]==0 and board[5]==-1 and board[8]==-1:
        return 2
    #diagonals
    if board[0]==-1 and board[4]==-1 and board[8]==0:
        return 8
    if board[0]==-1 and board[4]==0 and board[8]==-1:
        return 4
    if board[0]==0 and board[4]==-1 and board[8]==-1:
        return 0

    if board[2]==-1 and board[4]==-1 and board[6]==0:
        return 6
    if board[2]==-1 and board[4]==0 and board[6]==-1:
        return 4
    if board[2]==0 and board[4]==-1 and board[6]==-1:
        return 2
    return -1

def block():
    # top row
    if board[0] == 1 and board[1] == 1 and board[2] == 0:
        return 2
    if board[0] == 1 and board[1] == 0 and board[2] == 1:
        return 1
    if board[0] == 0 and board[1] == 1 and board[2] == 1:
        return 0
    # middle row
    if board[3] == 1 and board[4] == 1 and board[5] == 0:
        return 5
    if board[3] == 1 and board[4] == 0 and board[5] == 1:
        return 4
    if board[3] == 0 and board[4] == 1 and board[5] == 1:
        return 3
    # bottom row
    if board[6] == 1 and board[7] == 1 and board[8] == 0:
        return 8
    if board[6] == 1 and board[7] == 0 and board[8] == 1:
        return 7
    if board[6] == 0 and board[7] == 1 and board[8] == 1:
        return 6
    # verticle
    # left colom
    if board[0] == 1 and board[3] == 1 and board[6] == 0:
        return 6
    if board[0] == 1 and board[3] == 0 and board[6] == 1:
        return 3
    if board[0] == 0 and board[3] == 1 and board[6] == 1:
        return 0
    # middle colom
    if board[1] == 1 and board[4] == 1 and board[7] == 0:
        return 7
    if board[1] == 1 and board[4] == 0 and board[7] == 1:
        return 4
    if board[1] == 0 and board[4] == 1 and board[7] == 1:
        return 1
    # right colom
    if board[2] == 1 and board[5] == 1 and board[8] == 0:
        return 8
    if board[2] == 1 and board[5] == 0 and board[8] == 1:
        return 5
    if board[2] == 0 and board[5] == 1 and board[8] == 1:
        return 2
    # diagonals
    if board[0] == 1 and board[4] == 1 and board[8] == 0:
        return 8
    if board[0] == 1 and board[4] == 0 and board[8] == 1:
        return 4
    if board[0] == 0 and board[4] == 1 and board[8] == 1:
        return 0

    if board[2] == 1 and board[4] == 1 and board[6] == 0:
        return 6
    if board[2] == 1 and board[4] == 0 and board[6] == 1:
        return 4
    if board[2] == 0 and board[4] == 1 and board[6] == 1:
        return 2
    return 1

def opposetCorner():
    if board[0] == 1 and board[8] == 0:
        return 8
    if board[8]==1 and board[0]==0:
        return 0
    if board[2]==1 and board[6]==0:
        return 6
    if board[6]==1 and board[2]==0:
        return 2
    return -1

def emptyCorner():
    if board[8] == 0:
        return 8
    if board[0]==0:
        return 0
    if board[6]==0:
        return 6
    if board[2]==0:
        return 2
    return -1

def emptySide():
    if board[1] == 0:
        return 1
    if board[3]==0:
        return 3
    if board[5]==0:
        return 5
    if board[7]==0:
        return 7
    return -1