

def beginProgram():
    while True:
        print("\nChoose a Tic-Tac-Toe Game To Play: ")
        print(" 1. Two-Player Text User Interface")
        print(" 2. Two-Player Graphical User Interface")
        print(" 3. AI Text User Interface")
        print(" 4. AI Graphical User Interface")
        answer = int(input("Enter choice: "))

        if answer == 1:
           import TicTacToeText
        elif answer == 2:
            import TicTacToeGUI
        elif answer == 3:
            import TicTacToeTextAI
        elif answer == 4:
            import TicTacToeGUIAI
        else:
            print("Invalid Input")
            print("Please Try Again")

beginProgram()