gameBoard =[["*","*","*"], ["*","*","*"],["*","*","*"]]
runLoop = 1

def printBoard():
    print("")
    for row in gameBoard:
        for column in row:
            print(column, end = " ")
        print("")

def playerTurn(player):
    if player == 1:
        print("\nPLayer One's Turn")
    else: 
        print("\nPlayer Two's Turn")

    row = int(input("Enter row: ")) - 1
    column = int(input("Enter column: ")) - 1


    if row >= 0 and row <= 2 and column >= 0 and column <=2:
        if gameBoard[row][column] == "*":
            if player == 1:
                gameBoard[row][column] = "X"
            else: 
                gameBoard[row][column]= "O"
        else:
            print("\nSpot is taken.")
            print("Please try again.")
            printBoard()
            playerTurn(player)
    else:
        print("\nSpot does not exist")
        print("Please try again.")
        printBoard()
        playerTurn(player)

def checkGameOver():
    if gameBoard[0][0] == "X" and gameBoard[0][1] == "X" and gameBoard[0][2] == "X":
        print("PLAYER ONE WINS")
        print("GAME OVER")
        exit()
    elif gameBoard[1][0] == "X" and gameBoard[1][1] == "X" and gameBoard[1][2] == "X":
        print("PLAYER ONE WINS")
        print("GAME OVER")
        exit()
    elif gameBoard[2][0] == "X" and gameBoard[2][1] == "X" and gameBoard[2][2] == "X":
        print("PLAYER ONE WINS")
        print("GAME OVER")
        exit()
    elif gameBoard[0][0] == "X" and gameBoard[1][0] == "X" and gameBoard[2][0] == "X":
        print("PLAYER ONE WINS")
        print("GAME OVER")
        exit()
    elif gameBoard[0][1] == "X" and gameBoard[1][1] == "X" and gameBoard[2][1] == "X":
        print("PLAYER ONE WINS")
        print("GAME OVER")
        exit()
    elif gameBoard[0][2] == "X" and gameBoard[1][2] == "X" and gameBoard[2][2] == "X":
        print("PLAYER ONE WINS")
        print("GAME OVER")
        exit()
    elif gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == "X":
        print("PLAYER ONE WINS")
        print("GAME OVER")
        exit()
    elif gameBoard[2][0] == "X" and gameBoard[1][1] == "X" and gameBoard[0][2] == "X":
        print("PLAYER ONE WINS")
        print("GAME OVER")
        exit()

    elif gameBoard[0][0] == "O" and gameBoard[0][1] == "O" and gameBoard[0][2] == "O":
        print("PLAYER TWO WINS")
        print("GAME OVER")
        exit()
    elif gameBoard[1][0] == "O" and gameBoard[1][1] == "O" and gameBoard[1][2] == "O":
        print("PLAYER TWO WINS")
        print("GAME OVER")
        exit()
    elif gameBoard[2][0] == "O" and gameBoard[2][1] == "O" and gameBoard[2][2] == "O":
        print("PLAYER TWO WINS")
        print("GAME OVER")
        exit()
    elif gameBoard[0][0] == "O" and gameBoard[1][0] == "O" and gameBoard[2][0] == "O":
        print("PLAYER TWO WINS")
        print("GAME OVER")
        exit()
    elif gameBoard[0][1] == "O" and gameBoard[1][1] == "O" and gameBoard[2][1] == "O":
        print("PLAYER TWO WINS")
        print("GAME OVER")
        exit()
    elif gameBoard[0][2] == "O" and gameBoard[1][2] == "O" and gameBoard[2][2] == "O":
        print("PLAYER TWO WINS")
        print("GAME OVER")
        exit()
    elif gameBoard[0][0] == "O" and gameBoard[1][1] == "O" and gameBoard[2][2] == "O":
        print("PLAYER TWO WINS")
        print("GAME OVER")
        exit()
    elif gameBoard[2][0] == "O" and gameBoard[1][1] == "O" and gameBoard[0][2] == "O":
        print("PLAYER TWO WINS")
        print("GAME OVER")
        exit()
    else: 
        count = 0
        for x in range(3):
            for y in range(3):
                if gameBoard[x][y] == "*":
                    count = 1
        if count == 0:
            print("TIE")
            print("GAME OVER")
            exit()



printBoard()
while runLoop == 1:
    playerTurn(1)
    printBoard()
    checkGameOver()
    playerTurn(2)
    printBoard()
    checkGameOver()

