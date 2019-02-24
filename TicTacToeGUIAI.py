import random #Used to generate random variables
from tkinter import * #Used to create the Graphical User Interface
from tkinter import messagebox
window=Tk()
gameBoard =[["*","*","*"], ["*","*","*"],["*","*","*"]] #Grid representing the game board
playerVariable = "X" #Player's value on grid
computerVariable = "O" #AI's value on gird 

window.title("Tic Tac Toe ")
window.geometry("350x200")

gameFrame = Frame(window)

#Initalizing area around game board
lbl=Label(gameFrame,text="Tic-Tac-Toe AI",font=('Helvetica','15'))
lbl.grid(row=0,column=0)
lbl=Label(gameFrame,text="Player: " + playerVariable,font=('Helvetica','10'))
lbl.grid(row=1,column=0)
lbl=Label(gameFrame,text="K.A.R.E.N: " + computerVariable,font=('Helvetica','10'))
lbl.grid(row=2,column=0)

turn=1 #For first person turn.

#Called when top left button is clicked
def clicked1():
    global turn
    if gameBoard[0][0]=="*":   #For getting the text of a button
        if turn==1:
            turn=2
            gameBoard[0][0]=playerVariable
            topLeftBox["text"]=gameBoard[0][0]
            check()
            computerTurn()
        elif turn==2:
            turn=1
            gameBoard[0][0]=computerVariable
            topLeftBox["text"]=gameBoard[0][0]
            check()
#Called when top middle button is clicked
def clicked2():
    global turn
    if gameBoard[0][1]=="*":
        if turn==1:
            turn=2
            gameBoard[0][1]=playerVariable
            topMiddleBox["text"]=gameBoard[0][1]
            check()
            computerTurn()
        elif turn==2:
            turn=1
            gameBoard[0][1]=computerVariable
            topMiddleBox["text"]=gameBoard[0][1]
            check()
#Called when top right button is clicked
def clicked3():
    global turn
    if gameBoard[0][2]=="*":
        if turn==1:
            turn=2
            gameBoard[0][2]=playerVariable
            topRightBox["text"]=gameBoard[0][2]
            check()
            computerTurn()
        elif turn==2:
            turn=1
            gameBoard[0][2]=computerVariable
            topRightBox["text"]=gameBoard[0][2]
            check()
#Called when center left button is clicked
def clicked4():
    global turn
    if gameBoard[1][0]=="*":
        if turn==1:
            turn=2
            gameBoard[1][0]=playerVariable
            centerLeftBox["text"]=gameBoard[1][0]
            check()
            computerTurn()
        elif turn==2:
            turn=1
            gameBoard[1][0]=computerVariable
            centerLeftBox["text"]=gameBoard[1][0]
            check()
#Called when center middle button is clicked
def clicked5():
    global turn
    if gameBoard[1][1]=="*":
        if turn==1:
            turn=2
            gameBoard[1][1]=playerVariable
            centerMiddleBox["text"]=gameBoard[1][1]
            check()
            computerTurn()
        elif turn==2:
            turn=1
            gameBoard[1][1]=computerVariable
            centerMiddleBox["text"]=gameBoard[1][1]
            check()
#Called when center right button is clicked
def clicked6():
    global turn
    if gameBoard[1][2]=="*":
        if turn==1:
            turn=2
            gameBoard[1][2]=playerVariable
            centerRightBox["text"]=gameBoard[1][2]
            check()
            computerTurn()
        elif turn==2:
            turn=1
            gameBoard[1][2]=computerVariable
            centerRightBox["text"]=gameBoard[1][2]
            check()
#Called when bottom left button is clicked
def clicked7():
    global turn
    if gameBoard[2][0]=="*":
        if turn==1:
            turn=2
            gameBoard[2][0]=playerVariable
            bottomLeftBox["text"]=gameBoard[2][0]
            check()
            computerTurn()
        elif turn==2:
            turn=1
            gameBoard[2][0]=computerVariable
            bottomLeftBox["text"]=gameBoard[2][0]
            check()
#Called when bottom middle button is clicked
def clicked8():
    global turn
    if gameBoard[2][1]=="*":
        if turn==1:
            turn=2
            gameBoard[2][1]=playerVariable
            bottomMiddleBox["text"]=gameBoard[2][1]
            check()
            computerTurn()
        elif turn==2:
            turn=1
            gameBoard[2][1]=computerVariable
            bottomMiddleBox["text"]=gameBoard[2][1]
            check()
#Called when bottom right button is clicked
def clicked9():
    global turn
    if gameBoard[2][2]=="*":
        if turn==1:
            turn=2
            gameBoard[2][2]=playerVariable
            bottomRightBox["text"]=gameBoard[2][2]
            check()
            computerTurn()
        elif turn==2:
            turn=1
            gameBoard[2][2]=computerVariable
            bottomRightBox["text"]=gameBoard[2][2]
            check()
tieFlag = 1 #Global variable to check if board is filled and used to determine a tie
#Function that checks if a player has won the game
def check():
    window.update()

    global tieFlag

    topLeftValue = gameBoard[0][0]
    topMiddleValue = gameBoard[0][1]
    topRightValue = gameBoard[0][2]
    centerLeftValue = gameBoard[1][0]
    centerMiddleValue = gameBoard[1][1]
    centerRightValue = gameBoard[1][2]
    bottomLeftValue = gameBoard[2][0]
    bottomMiddleValue = gameBoard[2][1]
    bottomRightValue = gameBoard[2][2]
    tieFlag=tieFlag+1
    
    #checks top row
    if topLeftValue==topMiddleValue and topLeftValue==topRightValue and topLeftValue=="O" or topLeftValue==topMiddleValue and topLeftValue==topRightValue and topLeftValue=="X":
        win(topLeftBox["text"])
    #checks center row
    elif centerLeftValue==centerMiddleValue and centerLeftValue==centerRightValue and centerLeftValue=="O" or centerLeftValue==centerMiddleValue and centerLeftValue==centerRightValue and centerLeftValue=="X":
        win(centerLeftBox["text"])
    #checks bottom row
    elif bottomLeftValue==bottomMiddleValue and bottomLeftValue==bottomRightValue and bottomLeftValue=="O" or bottomLeftValue==bottomMiddleValue and bottomLeftValue==bottomRightValue and bottomLeftValue=="X":
        win(bottomLeftBox["text"])
    #checks left column
    elif topLeftValue==centerLeftValue and topLeftValue==bottomLeftValue and topLeftValue=="O" or topLeftValue==centerLeftValue and topLeftValue==bottomLeftValue and topLeftValue=="X":
        win(topLeftBox["text"])
    #checks middle column
    elif topMiddleValue==centerMiddleValue and topMiddleValue==bottomMiddleValue and topMiddleValue=="O" or topMiddleValue==centerMiddleValue and topMiddleValue==bottomMiddleValue and topMiddleValue=="X":
        win(topMiddleBox["text"])
    #checks right column
    elif topRightValue==centerRightValue and topRightValue==bottomRightValue and topRightValue=="O" or topRightValue==centerRightValue and topRightValue==bottomRightValue and topRightValue=="X":
        win(topRightBox["text"])
    #checks left to right diagonal
    elif topLeftValue==centerMiddleValue and topLeftValue==bottomRightValue and topLeftValue=="O" or topLeftValue==centerMiddleValue and topLeftValue==bottomRightValue and topLeftValue=="X":
        win(topLeftBox["text"])
    #checks right to left diagonal
    elif bottomLeftValue==centerMiddleValue and bottomLeftValue==topRightValue and bottomLeftValue=="O" or bottomLeftValue==centerMiddleValue and bottomLeftValue==topRightValue and bottomLeftValue=="X":
        win(bottomLeftBox["text"])
    else:
        if tieFlag==10:
            messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
            window.destroy()

#Prints out the winner of the game to the screen
def win(winner):
    win = None
    if winner == playerVariable:
        win = "YOU WIN"
    elif winner == computerVariable:
        win = "K.A.R.E.N WINS"
    messagebox.showinfo("GAME OVER", win)
    window.destroy()  # is used to close the program

#This is the function that holds the algorithim that allows the AI to choose its move 
def computerTurn():
    global turn
    #print(turn)

    turnTaken = 0 #variable to determine of turn has been taken

    topLeft = gameBoard[0][0]
    topMiddle = gameBoard[0][1]
    topRight = gameBoard[0][2]
    centerLeft = gameBoard[1][0]
    centerMiddle = gameBoard[1][1]
    centerRight = gameBoard[1][2]
    bottomLeft = gameBoard[2][0]
    bottomMiddle = gameBoard[2][1]
    bottomRight = gameBoard[2][2]

    #Check for Winning Move 
    if turnTaken == 0:
        #Check Left Column
        if topLeft==computerVariable and topLeft==centerLeft and bottomLeft=="*":
            turnTaken=1
            clicked7()
        elif topLeft==computerVariable and topLeft==bottomLeft and centerLeft=="*":
            turnTaken=1
            clicked4()
        elif centerLeft==computerVariable and centerLeft==bottomLeft and topLeft=="*":
            turnTaken=1
            clicked1()
        #Check Middle Column
        elif topMiddle==computerVariable and topMiddle==centerMiddle and bottomMiddle=="*":
            turnTaken=1
            clicked8()
        elif topMiddle==computerVariable and topMiddle==bottomMiddle and centerMiddle=="*":
            turnTaken=1
            clicked5()
        elif centerMiddle==computerVariable and centerMiddle==bottomMiddle and topMiddle=="*":
            turnTaken=1
            clicked2()
        #Check Right Column
        elif topRight==computerVariable and topRight==centerRight and bottomRight=="*":
            turnTaken=1
            clicked9()
        elif topRight==computerVariable and topRight==bottomRight and centerRight=="*":
            turnTaken=1
            clicked6()
        elif centerRight==computerVariable and centerRight==bottomRight and topRight=="*":
            turnTaken=1
            clicked3()
        #Check Top Row
        elif topLeft==computerVariable and topLeft==topMiddle and topRight=="*":
            turnTaken=1
            clicked3()
        elif topLeft==computerVariable and topLeft==topRight and topMiddle=="*":
            turnTaken=1
            clicked2()
        elif topMiddle==computerVariable and topMiddle==topRight and topLeft=="*":
            turnTaken=1
            clicked1()
        #Check Middle Row
        elif centerLeft==computerVariable and centerLeft==centerMiddle and centerRight=="*":
            turnTaken=1
            clicked6()
        elif centerLeft==computerVariable and centerLeft==centerRight and centerMiddle=="*":
            turnTaken=1
            clicked5()
        elif centerMiddle==computerVariable and centerMiddle==centerRight and centerLeft=="*":
            turnTaken=1
            clicked4()
        #Check Bottom Row
        elif bottomLeft==computerVariable and bottomLeft==bottomMiddle and bottomRight=="*":
            turnTaken=1
            clicked9()
        elif bottomLeft==computerVariable and bottomLeft==bottomRight and bottomMiddle=="*":
            turnTaken=1
            clicked8()
        elif bottomMiddle==computerVariable and bottomMiddle==bottomRight and bottomLeft=="*":
            turnTaken=1
            clicked7()
        #Check Left Diagonal
        elif topLeft==computerVariable and topLeft==centerMiddle and bottomRight=="*":
            turnTaken=1
            clicked9()
        elif topLeft==computerVariable and topLeft==bottomRight and centerMiddle=="*":
            turnTaken=1
            clicked5()
        elif centerMiddle==computerVariable and centerMiddle==bottomRight and topLeft=="*":
            turnTaken=1
            clicked1()
        #Check Right Diagonal
        elif topRight==computerVariable and topRight==centerMiddle and bottomLeft=="*":
            turnTaken=1
            clicked7()
        elif topRight==computerVariable and topRight==bottomLeft and centerMiddle=="*":
            turnTaken=1
            clicked5()
        elif centerMiddle==computerVariable and centerMiddle==bottomLeft and topRight=="*":
            turnTaken=1
            clicked3()
        #if turnTaken == 1:
            #print("Win move taken")

    #Check for Blocking User Win Move 
    if turnTaken == 0:
        #Check Left Column
        if topLeft==playerVariable and topLeft==centerLeft and bottomLeft=="*":
            turnTaken=1
            clicked7()
        elif topLeft==playerVariable and topLeft==bottomLeft and centerLeft=="*":
            turnTaken=1
            clicked4()
        elif centerLeft==playerVariable and centerLeft==bottomLeft and topLeft=="*":
            turnTaken=1
            clicked1()
        #Check Middle Column
        elif topMiddle==playerVariable and topMiddle==centerMiddle and bottomMiddle=="*":
            turnTaken=1
            clicked8()
        elif topMiddle==playerVariable and topMiddle==bottomMiddle and centerMiddle=="*":
            turnTaken=1
            clicked5()
        elif centerMiddle==playerVariable and centerMiddle==bottomMiddle and topMiddle=="*":
            turnTaken=1
            clicked2()
        #Check Right Column
        elif topRight==playerVariable and topRight==centerRight and bottomRight=="*":
            turnTaken=1
            clicked9()
        elif topRight==playerVariable and topRight==bottomRight and centerRight=="*":
            turnTaken=1
            clicked6()
        elif centerRight==playerVariable and centerRight==bottomRight and topRight=="*":
            turnTaken=1
            clicked3()
        #Check Top Row
        elif topLeft==playerVariable and topLeft==topMiddle and topRight=="*":
            turnTaken=1
            clicked3()
        elif topLeft==playerVariable and topLeft==topRight and topMiddle=="*":
            turnTaken=1
            clicked2()
        elif topMiddle==playerVariable and topMiddle==topRight and topLeft=="*":
            turnTaken=1
            clicked1()
        #Check Middle Row
        elif centerLeft==playerVariable and centerLeft==centerMiddle and centerRight=="*":
            turnTaken=1
            clicked6()
        elif centerLeft==playerVariable and centerLeft==centerRight and centerMiddle=="*":
            turnTaken=1
            clicked5()
        elif centerMiddle==playerVariable and centerMiddle==centerRight and centerLeft=="*":
            turnTaken=1
            clicked4()
        #Check Bottom Row
        elif bottomLeft==playerVariable and bottomLeft==bottomMiddle and bottomRight=="*":
            turnTaken=1
            clicked9()
        elif bottomLeft==playerVariable and bottomLeft==bottomRight and bottomMiddle=="*":
            turnTaken=1
            clicked8()
        elif bottomMiddle==playerVariable and bottomMiddle==bottomRight and bottomLeft=="*":
            turnTaken=1
            clicked7()
        #Check Left Diagonal
        elif topLeft==playerVariable and topLeft==centerMiddle and bottomRight=="*":
            turnTaken=1
            clicked9()
        elif topLeft==playerVariable and topLeft==bottomRight and centerMiddle=="*":
            turnTaken=1
            clicked5()
        elif centerMiddle==playerVariable and centerMiddle==bottomRight and topLeft=="*":
            turnTaken=1
            clicked1()
        #Check Right Diagonal
        elif topRight==playerVariable and topRight==centerMiddle and bottomLeft=="*":
            turnTaken=1
            clicked7()
        elif topRight==playerVariable and topRight==bottomLeft and centerMiddle=="*":
            turnTaken=1
            clicked5()
        elif centerMiddle==playerVariable and centerMiddle==bottomLeft and topRight=="*":
            turnTaken=1
            clicked3()
        #if turnTaken == 1:
            #print("Block move taken")

    #Checking for a Corner move
    if turnTaken == 0:
        possible_corners = [[0,0],[0,2],[2,0],[2,2]]
        random.shuffle(possible_corners)
        #for x in range(len(possible_corners)): 
            #print (possible_corners[x])

        while len(possible_corners) > 0:
            possibleCorner = possible_corners.pop(0)
            if gameBoard[possibleCorner[0]][possibleCorner[1]]=="*":
                #gameBoard[possibleCorner[0]][possibleCorner[1]]=computerVariable
                turnTaken=1
                if possibleCorner[0] == 0 and possibleCorner[1] == 0:
                    clicked1()
                elif possibleCorner[0] == 0 and possibleCorner[1] == 2:
                    clicked3()
                elif possibleCorner[0] == 2 and possibleCorner[1] == 0:
                    clicked7()
                elif possibleCorner[0] == 2 and possibleCorner[1] == 2:
                    clicked9()
                #print("Corner move taken")
                break
            
    #Checking for Center move
    if turnTaken == 0:
        if centerMiddle == "*":
            turnTaken=1
            clicked5()
            #print("Center move taken")
    
    #Checking for Side moves
    if turnTaken == 0:
        possible_sides = [[0,1],[1,0],[1,2],[2,1]]
        random.shuffle(possible_sides)
        #for x in range(len(possible_sides)): 
            #print (possible_sides[x])

        while len(possible_sides) > 0:
            possibleSide = possible_sides.pop(0)
            if gameBoard[possibleSide[0]][possibleSide[1]]=="*":
                turnTaken=1
                if possibleSide[0] == 0 and possibleSide[1] == 1:
                    clicked2()
                elif possibleSide[0] == 1 and possibleSide[1] == 0:
                    clicked4()
                elif possibleSide[0] == 1 and possibleSide[1] == 2:
                    clicked6()
                elif possibleSide[0] == 2 and possibleSide[1] == 1:
                    clicked8()
                #print("Side move taken")
                break

#Initalizes the buttons that represent the game board in a grid on the GUI window
topLeftBox = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
topLeftBox.grid(column=1, row=1)
topMiddleBox = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
topMiddleBox.grid(column=2, row=1)
topRightBox = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
topRightBox.grid(column=3, row=1)
centerLeftBox = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked4)
centerLeftBox.grid(column=1, row=2)
centerMiddleBox = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked5)
centerMiddleBox.grid(column=2, row=2)
centerRightBox = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked6)
centerRightBox.grid(column=3, row=2)
bottomLeftBox = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked7)
bottomLeftBox.grid(column=1, row=3)
bottomMiddleBox = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked8)
bottomMiddleBox.grid(column=2, row=3)
bottomRightBox = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked9)
bottomRightBox.grid(column=3, row=3)

#Function that runs game in a loop until the game is over
def startGame():
    gameFrame.pack()
    window.mainloop()

startGame()#Starts the game