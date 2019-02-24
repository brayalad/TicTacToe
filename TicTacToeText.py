#Two player game of Tic-Tac-Toe where each player gets a 
#turn after the other. Uses a console text interface

gameBoard = None #Grid that represents the game board

#Prints out the game board to the console
def printBoard():
    rowString = ["R","O","W"]
    rowCount = 0

    print("")
    print("      C   O   L")
    print("      1   2   3")
    print("    - - - - - - -")
    for row in gameBoard:
        print(rowString[rowCount]+" "+str((rowCount+1)), end=" | ")
        rowCount += 1
        for column in row:
            print(column, end=" | ")
        print("\n    - - - - - - -")

#Function that allows the player to take their turn
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

#Function that checks if a player has won the game
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
    #Checks top row 
    if tL==tM and tL==tR and tL=="O" or tL==tM and tL==tR and tL=="X":
        winner(tL)
    #Checks center row
    elif cL==cM and cL==cR and cL=="O" or cL==cM and cL==cR and cL=="X":
        winner(cL)
    #Checks bottom row
    elif bL==bM and bL==bR and bL=="O" or bL==bM and bL==bR and bL=="X":
        winner(bL)
    #Checks left column
    elif tL==cL and tL==bL and tL=="O" or tL==cL and tL==bL and tL=="X":
        winner(tL)
    #Checks middle column
    elif tM==cM and tM==bM and tM=="O" or tM==cM and tM==bM and tM=="X":
        winner(tM)
    #Checks right column
    elif tR==cR and tR==bR and tR=="O" or tR==cR and tR==bR and tR=="X":
        winner(tR)
    #Checks left to right diagonal
    elif tL==cM and tL==bR and tL=="O" or tL==cM and tL==bR and tL=="X":
        winner(tL)
    #Checks right to left diagonal
    elif bL==cM and bL==tR and bL=="O" or bL==cM and bL==tR and bL=="X":
        winner(bL)
    else: 
        count = 0
        for x in range(3):
            for y in range(3):
                if gameBoard[x][y] == "*":
                    count = 1
        if count == 0:
            print("\nTIE")
            print("GAME OVER\n")
            gameOver()

#If a winner is determined, the game is ended and user is allowed to start a new game
def winner(player):
    if player == "X":
        print("\nPLAYER ONE WINS")
    elif player == "O":
        print("\nPLAYER TWO WINS")
    print("GAMEOVER\n")
    gameOver()

#Initalized the game board grid and prints out the rules and instructions to the user
def initalizeGame():
    global gameBoard
    gameBoard = [["*","*","*"], ["*","*","*"],["*","*","*"]] 

    print("\nHere are the rules:")
    print(" You will be playing eachother until a winner is determined.")
    print(" 3 of your symbols must be placeed together inorder to win.")
    print(" Symbols can be placed by row, columns, or diagonaly.")
    print(" Rows go from left to right. Columns from top to down.")
    print(" First to 3 symbols placed together wins")
    print("\nLet The Game Begin!\n")

    startGame()

#Asks user it they would like to start a new game, if so, the game is initialized
def startNewGame():
    print("Would you like to start a new game?")
    print(" 1. Yes")
    print(" 2. No")
    choice = int(input("Enter choice: "))

    if choice == 1:
        initalizeGame()
    elif choice == 2:
        print("Thank you for playing!\n")
        exit()
    else:
        print("\nInvalid Option.\nPlease Try Again.\n")
        startNewGame()

#Called when the game is over and calls the start new game function
def gameOver():
    startNewGame()

#Function that starts the game and runs the game on a while loop until it is over
def startGame():
    printBoard()
    while True:
        playerTurn(1)
        printBoard()
        checkGameOver()
        playerTurn(2)
        printBoard()
        checkGameOver()

#Main function where the program begins
def main():
    print("\nWelcome To Tic-Tac-Toe!\nTwo-Player Edition\n")
    startNewGame()

main()#Starts the program

