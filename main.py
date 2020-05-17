import random
def displayBoard(boardList):
    print("-----------")
    print("| "+boardList[7]+" | "+boardList[8]+" | "+boardList[9]+" |")
    print("-------------")
    print("| "+boardList[4]+" | "+boardList[5]+" | "+boardList[6]+" |")
    print("-------------")
    print("| "+boardList[1]+" | "+boardList[2]+" | "+boardList[3]+" |")
    print("-----------")

def playerMove(board):
    while True:
        x=int(input("What is your move :"))
        if x in [1,2,3,4,5,6,7,8,9] and board[x]=="":
            return x
            
def checkWinner(boardList,letter):
    if((boardList[1]==letter and boardList[2]==letter and boardList[3]==letter) or #check horizontal
       (boardList[4]==letter and boardList[5]== letter and boardList[6]==letter ) or
       (boardList[7]==letter and boardList[8]==letter and boardList[9]==letter) or
       (boardList[1]==letter and boardList[5]==letter and boardList[9]==letter) or #check diagonal
       (boardList[3]==letter and boardList[5]==letter and boardList[7]==letter) or
       (boardList[1]==letter and boardList[4]==letter and boardList[7]==letter) or #check vertical
       (boardList[2]==letter and boardList[5]==letter and boardList[8]==letter) or
       (boardList[3]==letter and boardList[6]==letter and boardList[9]==letter)):
        return True
    else:
        return False
def checkFreeSpace(boardList,move):
    return boardList[move]==""

def getBoardCopy(board):
    dupeBoard=[]

    for i in board:
        dupeBoard.append(i)

    return dupeBoard
def checkdraw(boardList):
    for i in range(1,10):
        if checkFreeSpace(boardList,i):
            return False
    return True

def computerMove(boardList,cL,pL):
    for i in range(1,10):
        copyBoard=getBoardCopy(boardList)
        if checkFreeSpace(copyBoard,i):
            copyBoard[i]=cL
            if checkWinner(copyBoard,cL):
                return i
    for i in range(1,10):
        copyBoard=getBoardCopy(boardList)
        if checkFreeSpace(copyBoard,i):
            copyBoard[i]=pL
            if checkWinner(copyBoard,pL):
                return i
    tList=[]
    found=0
    for i in [1,3,7,9]:
        copyBoard=getBoardCopy(boardList)
        if copyBoard[i]=="":
            tList.append(i)
            found=1
    if found==1:
        return random.choice(tList)
    if boardList[5]=="":
        return 5
    for i in [2,4,6,8]:
        copyBoard=getBoardCopy(boardList)
        if copyBoard[i]=="":
            tList.append(i)
    return random.choice(tList)   


def firstMove():
    return random.randint(1,2)
def playerChoice():
    print("X or O")
    if input().upper()=="X":
        return ["X","O"]
    else:
        return ["O","X"]

print("------------ Tic Tac Toe ------------")
youS=computerS=d=0
while True:
    board=[""]*10
    gameStatus=True
    x=firstMove()
    gameStatus=True
    playerLetter,computerLetter=playerChoice()
    if x==1:
        turn="player"
    else:
        turn="computer"
    print("'{}' goes First".format(turn))
    while gameStatus:
        
        if turn=="player":
            displayBoard(board)
            y=playerMove(board)
            board[y]=playerLetter
            if checkWinner(board,playerLetter):
                displayBoard(board)
                print("You win!!!!")
                youS=youS+1
                gameStatus=False
            if checkdraw(board)==True:
                displayBoard(board)
                d=d+1
                print("-----Draw-----")
                gameStatus=False
            turn="computer"
        else:
            
            x=computerMove(board,computerLetter,playerLetter)
            board[x]=computerLetter
            if checkWinner(board,computerLetter):
                displayBoard(board)
                print("computer win!!!!")
                computerS=computerS+1
                gameStatus=False
            elif checkdraw(board):
                displayBoard(board)
                d=d+1
                print("-----Draw-----")
                gameStatus=False
            else:
                turn="player"
    if not gameStatus:
        if input("do you like to play again 'y' or 'n'")=="y":
            continue
        else:
            print("computer: "+str(computerS)+" draw: "+str(d)+" you: "+str(youS))
            break

    
