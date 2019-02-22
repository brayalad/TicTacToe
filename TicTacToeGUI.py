from tkinter import *
from tkinter import messagebox
window=Tk()
gameBoard =[["*","*","*"], ["*","*","*"],["*","*","*"]]

window.title("Tic Tac Toe ")
window.geometry("500x400")

lbl=Label(window,text="Tic-tac-toe Game",font=('Helvetica','15'))
lbl.grid(row=0,column=0)
lbl=Label(window,text="Player 1: X",font=('Helvetica','10'))
lbl.grid(row=1,column=0)
lbl=Label(window,text="Player 2: O",font=('Helvetica','10'))
lbl.grid(row=2,column=0)

turn=1; #For first person turn.

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
flag = 1
def check():
    global flag
    tL = gameBoard[0][0]
    tM = gameBoard[0][1]
    tR = gameBoard[0][2]
    cL = gameBoard[1][0]
    cM = gameBoard[1][1]
    cR = gameBoard[1][2]
    bL = gameBoard[2][0]
    bM = gameBoard[2][1]
    bR = gameBoard[2][2]
    flag=flag+1
    if tL==tM and tL==tR and tL=="O" or tL==tM and tL==tR and tL=="X":
        win(topLeft["text"])
    if cL==cM and cL==cR and cL=="O" or cL==cM and cL==cR and cL=="X":
        win(centerLeft["text"])
    if bL==bM and bL==bR and bL=="O" or bL==bM and bL==bR and bL=="X":
        win(bottomLeft["text"])
    if tL==cL and tL==bL and tL=="O" or tL==cL and tL==bL and tL=="X":
        win(topLeft["text"])
    if tM==cM and tM==bM and tM=="O" or tM==cM and tM==bM and tM=="X":
        win(topMiddle["text"])
    if tR==cR and tR==bR and tR=="O" or tR==cR and tR==bR and tR=="X":
        win(topRight["text"])
    if tL==cM and tL==bR and tL=="O" or tL==cM and tL==bR and tL=="X":
        win(topLeft["text"])
    if bL==cM and bL==tR and bL=="O" or bL==cM and bL==tR and bL=="X":
        win(bottomLeft["text"])
    if flag ==10:
        messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
        window.destroy()

def win(player):
    ans = "Game complete " +player + " wins ";
    messagebox.showinfo("Congratulations", ans)
    window.destroy()  # is used to close the program


topLeft = Button(window, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
topLeft.grid(column=1, row=1)
topMiddle = Button(window, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
topMiddle.grid(column=2, row=1)
topRight = Button(window, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
topRight.grid(column=3, row=1)
centerLeft = Button(window, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked4)
centerLeft.grid(column=1, row=2)
centerMiddle = Button(window, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked5)
centerMiddle.grid(column=2, row=2)
centerRight = Button(window, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked6)
centerRight.grid(column=3, row=2)
bottomLeft = Button(window, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked7)
bottomLeft.grid(column=1, row=3)
bottomMiddle = Button(window, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked8)
bottomMiddle.grid(column=2, row=3)
bottomRight = Button(window, text=" ",bg="blue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked9)
bottomRight.grid(column=3, row=3)


def startGame():
    window.mainloop()

startGame()