

def beginProgram():
    runLoop = 1
    while(runLoop == 1):
        print("Choose a Tic-Tac-Toe Interface: ")
        print("1. Text Interface")
        print("2. Graphical User Interface")
        answer = int(input("Enter choice: "))

        if answer == 1:
           import TicTacToeText
        elif answer == 2:
            import TicTacToeGUI
        else:
            print("Invalid Input")
            print("Please Try Again")

beginProgram()