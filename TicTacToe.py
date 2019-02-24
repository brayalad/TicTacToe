
#This program is a game of Tic-Tac-Toe
#This is the begining menu for the user to decide which edition
#of the Tic-Tac-Toe Game they would like to play. 
#There are two ways to play this game, each with two different interfaces
#The user can play a two-player game of Tic-Tac-Toe with either a text or graphical user interface
#The user can play a single-player game of Tic-Tac-Toe against the program's artfical intellegence 

def beginProgram():
    
    #Menu showing user their options
    print("\nChoose a Tic-Tac-Toe Game To Play: ")
    print(" 1. Two-Player Text User Interface")
    print(" 2. Two-Player Graphical User Interface")
    print(" 3. AI Text User Interface")
    print(" 4. AI Graphical User Interface")
    answer = int(input("Enter choice: "))

    #Runs the version of the game the player chooses
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

beginProgram() #Begins program