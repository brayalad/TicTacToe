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
    tL = gameBoard[0][0]
    tM = gameBoard[0][1]
    tR = gameBoard[0][2]
    cL = gameBoard[1][0]
    cM = gameBoard[1][1]
    cR = gameBoard[1][2]
    bL = gameBoard[2][0]
    bM = gameBoard[2][1]
    bR = gameBoard[2][2]
    if tL==tM and tL==tR and tL=="O" or tL==tM and tL==tR and tL=="X":
        winner(tL)
    elif cL==cM and cL==cR and cL=="O" or cL==cM and cL==cR and cL=="X":
        winner(cL)
    elif bL==bM and bL==bR and bL=="O" or bL==bM and bL==bR and bL=="X":
        winner(bL)
    elif tL==cL and tL==bL and tL=="O" or tL==cL and tL==bL and tL=="X":
        winner(tL)
    elif tM==cM and tM==bM and tM=="O" or tM==cM and tM==bM and tM=="X":
        winner(tM)
    elif tR==cR and tR==bR and tR=="O" or tR==cR and tR==bR and tR=="X":
        winner(tR)
    elif tL==cM and tL==bR and tL=="O" or tL==cM and tL==bR and tL=="X":
        winner(tL)
    elif bL==cM and bL==tR and bL=="O" or bL==cM and bL==tR and bL=="X":
        winner(bL)
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

def winner(player):
    print("PLAYER " + player + " WINS")
    print("GAMEOVER")
    exit()

def startGame():
    printBoard()
    while runLoop == 1:
        playerTurn(1)
        printBoard()
        checkGameOver()
        playerTurn(2)
        printBoard()
        checkGameOver()

startGame()

