import tkinter

gameBoard =[["*","*","*"], ["*","*","*"],["*","*","*"]]

# creating basic window
window = tkinter.Tk()
window.geometry("312x324") # size of the window width:- 500, height:- 375
window.resizable(0, 0) # this prevents from resizing the window
window.title("Tic Tac Toe")


def player_turn():
    gameBoard[0][0] = "X"
    tkinter.Label(window, text = "HI").pack()


tkinter.Label(window, text="1").grid(row = 0)

upperLeftCorner = tkinter.Button(window, text=gameBoard[0][0], command=player_turn).grid(row=0,column=1)
upperMiddle = tkinter.Button(window, text=gameBoard[0][1]).grid(row=0,column=2)
upperRightCorner = tkinter.Button(window, text=gameBoard[0][2]).grid(row=0,column=3)


tkinter.Label(window, text="2").grid(row = 1)

centerLeft = tkinter.Button(window, text=gameBoard[1][0]).grid(row=1,column=1)
centerMiddle = tkinter.Button(window, text=gameBoard[1][1]).grid(row=1,column=2)
centerRight = tkinter.Button(window, text=gameBoard[1][2]).grid(row=1,column=3)


tkinter.Label(window, text="3").grid(row = 2)

lowerLeftCorner = tkinter.Button(window, text=gameBoard[2][0]).grid(row=2,column=1)
lowerMiddle = tkinter.Button(window, text=gameBoard[2][1]).grid(row=2,column=2)
lowerRightCorner = tkinter.Button(window, text=gameBoard[2][2]).grid(row=2,column=3)












window.mainloop()