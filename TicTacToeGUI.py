#Two player game of Tic-Tac-Toe where each player gets a 
#turn after the other. Uses a graphical user interface

from tkinter import * #Used to create the Graphical User Interface
from tkinter import messagebox
window=Tk() #Window that will hold the game
gameBoard =[["*","*","*"], ["*","*","*"],["*","*","*"]] #Grid representing the game board

window.title("Tic Tac Toe ")
window.geometry("350x200")

gameFrame = Frame(window)

#Setting up the text around the game board in GUI
lbl=Label(gameFrame,text="Tic-Tac-Toe Two-Player",font=('Helvetica','15'))
lbl.grid(row=0,column=0)
lbl=Label(gameFrame,text="Player 1: X",font=('Helvetica','10'))
lbl.grid(row=1,column=0)
lbl=Label(gameFrame,text="Player 2: O",font=('Helvetica','10'))
lbl.grid(row=2,column=0)


turn=1 #For first person turn.

#Called when user clicks top left buttom
def clicked1():
    global turn
    if gameBoard[0][0]=="*":   #For getting the text of a button
        if turn==1:
            turn=2
            gameBoard[0][0]="X"
            topLeft["text"]=gameBoard[0][0]
        elif turn==2:
            turn=1
            gameBoard[0][0]="O"
            topLeft["text"]=gameBoard[0][0]
        check()
#Called when user clicks top middle button
def clicked2():
    global turn
    if gameBoard[0][1]=="*":
        if turn==1:
            turn=2
            gameBoard[0][1]="X"
            topMiddle["text"]=gameBoard[0][1]
        elif turn==2:
            turn=1
            gameBoard[0][1]="O"
            topMiddle["text"]=gameBoard[0][1]
        check()
#Called when user clicks top right button
def clicked3():
    global turn
    if gameBoard[0][2]=="*":
        if turn==1:
            turn=2
            gameBoard[0][2]="X"
            topRight["text"]=gameBoard[0][2]
        elif turn==2:
            turn=1
            gameBoard[0][2]="O"
            topRight["text"]=gameBoard[0][2]
        check()
#Called when user clicks center left button
def clicked4():
    global turn
    if gameBoard[1][0]=="*":
        if turn==1:
            turn=2
            gameBoard[1][0]="X"
            centerLeft["text"]=gameBoard[1][0]
        elif turn==2:
            turn=1
            gameBoard[1][0]="O"
            centerLeft["text"]=gameBoard[1][0]
        check()
#Called when user clicks center button
def clicked5():
    global turn
    if gameBoard[1][1]=="*":
        if turn==1:
            turn=2
            gameBoard[1][1]="X"
            centerMiddle["text"]=gameBoard[1][1]
        elif turn==2:
            turn=1
            gameBoard[1][1]="O"
            centerMiddle["text"]=gameBoard[1][1]
        check()
#Called when user clicks center right button
def clicked6():
    global turn
    if gameBoard[1][2]=="*":
        if turn==1:
            turn=2
            gameBoard[1][2]="X"
            centerRight["text"]=gameBoard[1][2]
        elif turn==2:
            turn=1
            gameBoard[1][2]="O"
            centerRight["text"]=gameBoard[1][2]
        check()
#Called when user clicks bottom left button
def clicked7():
    global turn
    if gameBoard[2][0]=="*":
        if turn==1:
            turn=2
            gameBoard[2][0]="X"
            bottomLeft["text"]=gameBoard[2][0]
        elif turn==2:
            turn=1
            gameBoard[2][0]="O"
            bottomLeft["text"]=gameBoard[2][0]
        check()
#Called when user clicks bottom middle button
def clicked8():
    global turn
    if gameBoard[2][1]=="*":
        if turn==1:
            turn=2
            gameBoard[2][1]="X"
            bottomMiddle["text"]=gameBoard[2][1]
        elif turn==2:
            turn=1
            gameBoard[2][1]="O"
            bottomMiddle["text"]=gameBoard[2][1]
        check()
#Called when user clicks bottom right button
def clicked9():
    global turn
    if gameBoard[2][2]=="*":
        if turn==1:
            turn=2
            gameBoard[2][2]="X"
            bottomRight["text"]=gameBoard[2][2]
        elif turn==2:
            turn=1
            gameBoard[2][2]="O"
            bottomRight["text"]=gameBoard[2][2]
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
        win(topLeft["text"])
    #checks center row
    elif centerLeftValue==centerMiddleValue and centerLeftValue==centerRightValue and centerLeftValue=="O" or centerLeftValue==centerMiddleValue and centerLeftValue==centerRightValue and centerLeftValue=="X":
        win(centerLeft["text"])
    #checks bottom row
    elif bottomLeftValue==bottomMiddleValue and bottomLeftValue==bottomRightValue and bottomLeftValue=="O" or bottomLeftValue==bottomMiddleValue and bottomLeftValue==bottomRightValue and bottomLeftValue=="X":
        win(bottomLeft["text"])
    #checks left column
    elif topLeftValue==centerLeftValue and topLeftValue==bottomLeftValue and topLeftValue=="O" or topLeftValue==centerLeftValue and topLeftValue==bottomLeftValue and topLeftValue=="X":
        win(topLeft["text"])
    #checks middle column
    elif topMiddleValue==centerMiddleValue and topMiddleValue==bottomMiddleValue and topMiddleValue=="O" or topMiddleValue==centerMiddleValue and topMiddleValue==bottomMiddleValue and topMiddleValue=="X":
        win(topMiddle["text"])
    #checks right column
    elif topRightValue==centerRightValue and topRightValue==bottomRightValue and topRightValue=="O" or topRightValue==centerRightValue and topRightValue==bottomRightValue and topRightValue=="X":
        win(topRight["text"])
    #checks left to right diagonal 
    elif topLeftValue==centerMiddleValue and topLeftValue==bottomRightValue and topLeftValue=="O" or topLeftValue==centerMiddleValue and topLeftValue==bottomRightValue and topLeftValue=="X":
        win(topLeft["text"])
    #checks right to left diagonal
    elif bottomLeftValue==centerMiddleValue and bottomLeftValue==topRightValue and bottomLeftValue=="O" or bottomLeftValue==centerMiddleValue and bottomLeftValue==topRightValue and bottomLeftValue=="X":
        win(bottomLeft["text"])
    else:
        if tieFlag==10:
            messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
            window.destroy()

#Prints out the winner to the screen
def win(player):
    winner = None
    if player == "X":
        winner = "PLAYER 1 WINS"
    elif player == "O":
        winner = "PLAYER 2 WINS"
    messagebox.showinfo("Congratulations", winner)
    window.destroy()  # is used to close the program

#Buttons used to represent the game board are place on a grid in the window of the game screen
topLeft = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
topLeft.grid(column=1, row=1)
topMiddle = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
topMiddle.grid(column=2, row=1)
topRight = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
topRight.grid(column=3, row=1)
centerLeft = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked4)
centerLeft.grid(column=1, row=2)
centerMiddle = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked5)
centerMiddle.grid(column=2, row=2)
centerRight = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked6)
centerRight.grid(column=3, row=2)
bottomLeft = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked7)
bottomLeft.grid(column=1, row=3)
bottomMiddle = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked8)
bottomMiddle.grid(column=2, row=3)
bottomRight = Button(gameFrame, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked9)
bottomRight.grid(column=3, row=3)

#Function that runs the game using a loop
def startGame():
    gameFrame.pack(expand=True)
    window.mainloop()

startGame() #starts program