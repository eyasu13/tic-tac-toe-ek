import random
def displayBoard(boardList):
    print("-------------")
    print("| "+boardList[9]+" | "+boardList[8]+" | "+boardList[7]+" |")
    print("-------------")
    print("| "+boardList[4]+" | "+boardList[5]+" | "+boardList[6]+" |")
    print("-------------")
    print("| "+boardList[1]+" | "+boardList[2]+" | "+boardList[3]+" |")
    print("-------------")

def playerMove(boardList,move,playerLetter):
    boardList[move]=playerLetter;

def checkWinner(boardList):
    if((boardList[1]==boardList[2]==boardList[3]) or #check horizontal
       (boardList[4]==boardList[5]==boardList[6]) or
       (boardList[7]==boardList[8]==boardList[9]) or
       (boardList[1]==boardList[5]==boardList[9]) or #check diagonal
       (boardList[3]==boardList[5]==boardList[7]) or
       (boardList[1]==boardList[4]==boardList[7]) or #check vertical
       (boardList[2]==boardList[5]==boardList[8]) or
       (boardList[3]==boardList[6]==boardList[9])):
        return True
    else:
        return False

def checkdraw(boardList):
    for i in range(1,10):
        if boardList[i]==" ":
            return False
    return True

def checkFreeSpace(boardList,move):
    return boardList[move]==""
    
#def computerMove(boardList,isFree):
#ee
def firstMove():
    return random.randint(1,2)
def playerChoice():
    print("X or O")
    if input().upper()=="X":
        return ["X","O"]
    else:
        return ["O","X"]
print("------------ Tic Tac Toe ------------")
playerLetter,computerLetter=playerChoice()
print(playerLetter)
while True:
    board=[""]*10
    gameStatus=True
    x=firstMove()
    if x==1:
        turn="player"
    else:
        turn="computer"
    print("'{}' goes First".format(turn))
