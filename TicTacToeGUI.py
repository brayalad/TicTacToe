import tkinter

gameBoard =[["*","*","*"], ["*","*","*"],["*","*","*"]]

# creating basic window
window = tkinter.Tk()
window.geometry("312x324") # size of the window width:- 500, height:- 375
window.resizable(0, 0) # this prevents from resizing the window
window.title("Tic Tac Toe")

tkinter.Label(window, text="1").grid(row = 0)

tkinter.Button(window, text="*").grid(row=0,column=1)
tkinter.Button(window, text="*").grid(row=0,column=2)
tkinter.Button(window, text="*").grid(row=0,column=3)


tkinter.Label(window, text="2").grid(row = 1)

tkinter.Button(window, text="*").grid(row=1,column=1)
tkinter.Button(window, text="*").grid(row=1,column=2)
tkinter.Button(window, text="*").grid(row=1,column=3)


tkinter.Label(window, text="3").grid(row = 2)

tkinter.Button(window, text="*").grid(row=2,column=1)
tkinter.Button(window, text="*").grid(row=2,column=2)
tkinter.Button(window, text="*").grid(row=2,column=3)


tkinter.Button(window, text="*").pack()

window.mainloop()