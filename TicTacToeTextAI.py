import random #Used to generate random variables

gameBoard = None #Variable to hold the grid representing the game board
playerVariable = None #Variable that represents the player
computerVariable = None #Variable that represents the AI

#Prints the game board to the console
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

#Allows the user to choose what symbol they wish to play as. Either "X" or "O"
def choosePlayingSymbol():
    global playerVariable
    global computerVariable

    print("\nChoose a playing symbol")
    print(" 1. X")
    print(" 2. O")
    choice = int(input("Enter choice: "))

    if choice == 1:
        playerVariable = "X"
        computerVariable = "O"
    elif choice == 2:
        playerVariable = "O"
        computerVariable = "X"
    else:
        print("Invalid Option.\nPlease Try Again.")
        choosePlayingSymbol()

#Functions that allows the player to take their turn 
def playerTurn():
    print("\nYour Turn")

    row = int(input("Enter row: ")) - 1
    column = int(input("Enter column: ")) - 1


    if row >= 0 and row <= 2 and column >= 0 and column <=2:
        if gameBoard[row][column] == "*":
                gameBoard[row][column] = playerVariable
        else:
            print("\nSpot is taken.")
            print("Please try again.")
            printBoard()
            playerTurn()
    else:
        print("\nSpot does not exist")
        print("Please try again.")
        printBoard()
        playerTurn()

#Function that checks if the game is over and someone has won
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
            printBoard()
            print("\nTIE")
            print("GAME OVER\n")
            gameOver()

#Called when a winner is determined and ends the game
def winner(player):
    printBoard()
    if player == playerVariable:
        print("\nYOU WIN")
    elif player == computerVariable:
        print("\nK.A.R.E.N WINS")
    print("GAMEOVER\n")
    gameOver()

#This is the function that holds the algorithim that allows the AI to choose its move 
def computerTurn():
    turnTaken = 0 #variable to determine if turn has been taken

    topLeft = gameBoard[0][0]
    topMiddle = gameBoard[0][1]
    topRight = gameBoard[0][2]
    centerLeft = gameBoard[1][0]
    centerMiddle = gameBoard[1][1]
    centerRight = gameBoard[1][2]
    bottomLeft = gameBoard[2][0]
    bottomMiddle = gameBoard[2][1]
    bottomRight = gameBoard[2][2]

    #Check for a winning move
    if turnTaken == 0:
        #Check Left Column
        if topLeft==computerVariable and topLeft==centerLeft and bottomLeft=="*":
            gameBoard[2][0]=computerVariable
            turnTaken=1
        elif topLeft==computerVariable and topLeft==bottomLeft and centerLeft=="*":
            gameBoard[1][0]=computerVariable
            turnTaken=1
        elif centerLeft==computerVariable and centerLeft==bottomLeft and topLeft=="*":
            gameBoard[0][0]=computerVariable
            turnTaken=1
        #Check Middle Column
        elif topMiddle==computerVariable and topMiddle==centerMiddle and bottomMiddle=="*":
            gameBoard[2][1]=computerVariable
            turnTaken=1
        elif topMiddle==computerVariable and topMiddle==bottomMiddle and centerMiddle=="*":
            gameBoard[1][1]=computerVariable
            turnTaken=1
        elif centerMiddle==computerVariable and centerMiddle==bottomMiddle and topMiddle=="*":
            gameBoard[0][1]=computerVariable
            turnTaken=1
        #Check Right Column
        elif topRight==computerVariable and topRight==centerRight and bottomRight=="*":
            gameBoard[2][2]=computerVariable
            turnTaken=1
        elif topRight==computerVariable and topRight==bottomRight and centerRight=="*":
            gameBoard[1][2]=computerVariable
            turnTaken=1
        elif centerRight==computerVariable and centerRight==bottomRight and topRight=="*":
            gameBoard[0][2]=computerVariable
            turnTaken=1
        #Check Top Row
        elif topLeft==computerVariable and topLeft==topMiddle and topRight=="*":
            gameBoard[0][2]=computerVariable
            turnTaken=1
        elif topLeft==computerVariable and topLeft==topRight and topMiddle=="*":
            gameBoard[0][1]=computerVariable
            turnTaken=1
        elif topMiddle==computerVariable and topMiddle==topRight and topLeft=="*":
            gameBoard[0][0]=computerVariable
            turnTaken=1
        #Check Middle Row
        elif centerLeft==computerVariable and centerLeft==centerMiddle and centerRight=="*":
            gameBoard[1][2]=computerVariable
            turnTaken=1
        elif centerLeft==computerVariable and centerLeft==centerRight and centerMiddle=="*":
            gameBoard[1][1]=computerVariable
            turnTaken=1
        elif centerMiddle==computerVariable and centerMiddle==centerRight and centerLeft=="*":
            gameBoard[1][0]=computerVariable
            turnTaken=1
        #Check Bottom Row
        elif bottomLeft==computerVariable and bottomLeft==bottomMiddle and bottomRight=="*":
            gameBoard[2][2]=computerVariable
            turnTaken=1
        elif bottomLeft==computerVariable and bottomLeft==bottomRight and bottomMiddle=="*":
            gameBoard[2][1]=computerVariable
            turnTaken=1
        elif bottomMiddle==computerVariable and bottomMiddle==bottomRight and bottomLeft=="*":
            gameBoard[2][0]=computerVariable
            turnTaken=1
        #Check Left Diagonal
        elif topLeft==computerVariable and topLeft==centerMiddle and bottomRight=="*":
            gameBoard[2][2]=computerVariable
            turnTaken=1
        elif topLeft==computerVariable and topLeft==bottomRight and centerMiddle=="*":
            gameBoard[1][1]=computerVariable
            turnTaken=1
        elif centerMiddle==computerVariable and centerMiddle==bottomRight and topLeft=="*":
            gameBoard[0][0]=computerVariable
            turnTaken=1
        #Check Right Diagonal
        elif topRight==computerVariable and topRight==centerMiddle and bottomLeft=="*":
            gameBoard[2][0]=computerVariable
            turnTaken=1
        elif topRight==computerVariable and topRight==bottomLeft and centerMiddle=="*":
            gameBoard[1][1]=computerVariable
            turnTaken=1
        elif centerMiddle==computerVariable and centerMiddle==bottomLeft and topRight=="*":
            gameBoard[0][2]=computerVariable
            turnTaken=1
        #if turnTaken == 1:
            #print("Win move taken")

    #Checks for a winning move by the user and blocks it
    if turnTaken == 0:
        #Check Left Column
        if topLeft==playerVariable and topLeft==centerLeft and bottomLeft=="*":
            gameBoard[2][0]=computerVariable
            turnTaken=1
        elif topLeft==playerVariable and topLeft==bottomLeft and centerLeft=="*":
            gameBoard[1][0]=computerVariable
            turnTaken=1
        elif centerLeft==playerVariable and centerLeft==bottomLeft and topLeft=="*":
            gameBoard[0][0]=computerVariable
            turnTaken=1
        #Check Middle Column
        elif topMiddle==playerVariable and topMiddle==centerMiddle and bottomMiddle=="*":
            gameBoard[2][1]=computerVariable
            turnTaken=1
        elif topMiddle==playerVariable and topMiddle==bottomMiddle and centerMiddle=="*":
            gameBoard[1][1]=computerVariable
            turnTaken=1
        elif centerMiddle==playerVariable and centerMiddle==bottomMiddle and topMiddle=="*":
            gameBoard[0][1]=computerVariable
            turnTaken=1
        #Check Right Column
        elif topRight==playerVariable and topRight==centerRight and bottomRight=="*":
            gameBoard[2][2]=computerVariable
            turnTaken=1
        elif topRight==playerVariable and topRight==bottomRight and centerRight=="*":
            gameBoard[1][2]=computerVariable
            turnTaken=1
        elif centerRight==playerVariable and centerRight==bottomRight and topRight=="*":
            gameBoard[0][2]=computerVariable
            turnTaken=1
        #Check Top Row
        elif topLeft==playerVariable and topLeft==topMiddle and topRight=="*":
            gameBoard[0][2]=computerVariable
            turnTaken=1
        elif topLeft==playerVariable and topLeft==topRight and topMiddle=="*":
            gameBoard[0][1]=computerVariable
            turnTaken=1
        elif topMiddle==playerVariable and topMiddle==topRight and topLeft=="*":
            gameBoard[0][0]=computerVariable
            turnTaken=1
        #Check Middle Row
        elif centerLeft==playerVariable and centerLeft==centerMiddle and centerRight=="*":
            gameBoard[1][2]=computerVariable
            turnTaken=1
        elif centerLeft==playerVariable and centerLeft==centerRight and centerMiddle=="*":
            gameBoard[1][1]=computerVariable
            turnTaken=1
        elif centerMiddle==playerVariable and centerMiddle==centerRight and centerLeft=="*":
            gameBoard[1][0]=computerVariable
            turnTaken=1
        #Check Bottom Row
        elif bottomLeft==playerVariable and bottomLeft==bottomMiddle and bottomRight=="*":
            gameBoard[2][2]=computerVariable
            turnTaken=1
        elif bottomLeft==playerVariable and bottomLeft==bottomRight and bottomMiddle=="*":
            gameBoard[2][1]=computerVariable
            turnTaken=1
        elif bottomMiddle==playerVariable and bottomMiddle==bottomRight and bottomLeft=="*":
            gameBoard[2][0]=computerVariable
            turnTaken=1
        #Check Left Diagonal
        elif topLeft==playerVariable and topLeft==centerMiddle and bottomRight=="*":
            gameBoard[2][2]=computerVariable
            turnTaken=1
        elif topLeft==playerVariable and topLeft==bottomRight and centerMiddle=="*":
            gameBoard[1][1]=computerVariable
            turnTaken=1
        elif centerMiddle==playerVariable and centerMiddle==bottomRight and topLeft=="*":
            gameBoard[0][0]=computerVariable
            turnTaken=1
        #Check Right Diagonal
        elif topRight==playerVariable and topRight==centerMiddle and bottomLeft=="*":
            gameBoard[2][0]=computerVariable
            turnTaken=1
        elif topRight==playerVariable and topRight==bottomLeft and centerMiddle=="*":
            gameBoard[1][1]=computerVariable
            turnTaken=1
        elif centerMiddle==playerVariable and centerMiddle==bottomLeft and topRight=="*":
            gameBoard[0][2]=computerVariable
            turnTaken=1
        #if turnTaken == 1:
            #print("Block move taken")

    #Randomly chooses a corner spot, if available 
    if turnTaken == 0:
        possible_corners = [[0,0],[0,2],[2,0],[2,2]]
        random.shuffle(possible_corners)
        #for x in range(len(possible_corners)): 
            #print (possible_corners[x])

        while len(possible_corners) > 0:
            possibleCorner = possible_corners.pop(0)
            if gameBoard[possibleCorner[0]][possibleCorner[1]]=="*":
                gameBoard[possibleCorner[0]][possibleCorner[1]]=computerVariable
                turnTaken=1
                #print("Corner move taken")
                break
            
    #Chooses the center spot, if available
    if turnTaken == 0:
        if centerMiddle == "*":
            gameBoard[1][1] = computerVariable
            turnTaken=1
            #print("Center move taken")
    
    #Randomly chooses a side spot, if available
    if turnTaken == 0:
        possible_sides = [[0,1],[1,0],[1,2],[2,1]]
        random.shuffle(possible_sides)
        #for x in range(len(possible_sides)): 
            #print (possible_sides[x])

        while len(possible_sides) > 0:
            possibleSide = possible_sides.pop(0)
            if gameBoard[possibleSide[0]][possibleSide[1]]=="*":
                gameBoard[possibleSide[0]][possibleSide[1]]=computerVariable
                turnTaken=1
                #print("Side move taken")
                break
    #Informs the user that the AI has taken it's turn
    if turnTaken == 1:
        print("\nK.A.R.E.N has taken her turn")



#Function starts the while loop that runs the game until the game is over
def startGame(firstTurn):

    if firstTurn == 0:
        printBoard()
        while True:
            playerTurn()
            #printBoard()
            checkGameOver()
            computerTurn()
            checkGameOver()
            printBoard()
    elif firstTurn == 1:
        while True:
            computerTurn()
            checkGameOver()
            printBoard()
            playerTurn()
            #printBoard()
            checkGameOver()

#Initalizes the game board and prints out rules and instructions to the user
def initalizeGame():
    global gameBoard
    gameBoard = [["*","*","*"], ["*","*","*"],["*","*","*"]] 

    print("\nHere are the rules:")
    print(" You will be playing against the AI known as K.A.R.E.N.")
    print(" The first turn will be chosen at random.")
    print(" 3 of your symbols must be placeed together inorder to win.")
    print(" Symbols can be placed by row, columns, or diagonaly.")
    print(" Rows go from left to right. Columns from top to down.")

    choosePlayingSymbol() #Player chooses their playing symbol
    firstTurn = random.randint(0,1) #Whoever goes first is decided at random

    if firstTurn == 0:
        print("\nYou Go First")
        startGame(firstTurn)
    elif firstTurn == 1:
        print("\nK.A.R.E.N Goes First")
        startGame(firstTurn)

#Function that asks user if they would like to start a new game
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

#Called when game is over and calls the start new game function
def gameOver():
    startNewGame()

#Main function and start of the whole program
def main():
    print("\nWelcome To Tic-Tac-Toe!\nAI Edition\n")
    startNewGame()

main() #starts the program

