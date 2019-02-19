gameBoard =[["*","*","*"], ["*","*","*"],["*","*","*"]]
runLoop = 1

def printBoard():
    for x in gameBoard:
        for y in x:
            print(y, end = " ")
        print()

def playerTurn(player):
    if player == 1:
        print("PLayer One's Turn")
    else: 
        print("Player Two's Turn")

    row = int(input("Enter row: ")) - 1
    column = int(input("Enter column: ")) - 1


    if player == 1:
        gameBoard[row][column] = "X"
    else: 
        gameBoard[row][column]= "O"


printBoard()
while runLoop == 1:
    playerTurn(1)
    printBoard()
    playerTurn(2)
    printBoard()