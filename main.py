import random
def displayBoard(boardList):
    print("-----------")
    print("| "+boardList[9]+" | "+boardList[8]+" | "+boardList[7]+" |")
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

def checkdraw(boardList):
    for i in range(1,10):
        if checkFreeSpace(boardList,i):
            return False
    return True

def computerMove(boardList,cL,pL):
    for i in range(1,10):
        copyBoard=boardList
        if checkFreeSpace(copyBoard,i):
            copyBoard[i]=cL
            if checkWinner(copyBoard,cL):
                return i
    for i in range(1,10):
        copyBoard=boardList
        if checkFreeSpace(copyBoard,i):
            copyBoard[i]=pL
            if checkWinner(copyBoard,pL):
                return i
    return 8


def firstMove():
    return random.randint(1,2)
def playerChoice():
    print("X or O")
    if input().upper()=="X":
        return ["X","O"]
    else:
        return ["O","X"]
print("------------ Tic Tac Toe ------------")
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
                print("You win!!!!")
                gameStatus=False
            if checkdraw(board)==True:
                print("-----Draw-----")
                gameStatus=False
            turn="computer"
        else:
            x=computerMove(board,computerLetter,playerLetter)
            board[x]=computerLetter
            displayBoard(board)
            if checkWinner(board,computerLetter):
                print("computer win!!!!")
                gameStatus=False
            elif checkdraw(board):
                print("-----Draw-----")
                gameStatus=False
            else:
                turn="player"

            
    

    
