# Introduction
print("\n\n**Hi and Welcome to Ray's Boom Boom Room!**\n\n")

# Start game function
def start():
    start = input("Would you like to play a game of rock paper scissors?\nEnter 'yes' to play: ")
    if start == "Yes" or start == "yes":
        game()
    else:
        print("\nOkay, have a nice day!")

# Number of rounds each player has won
P1 = 0
P2 = 0

# Game variables and functions
choice = ["rock", "scissors", "paper"]

def score(): # Prints updated scoreboard
    score = "    " + str(P1) + "-" + str(P2)
    print(score)
def game(): # The main game function.
    move()
    compare()
    restart()
def move(): # Lets each player make a move.
    print()
    print(choice)
    global p1
    p1 = input("\nPlayer 1. Choose your weapon: ")
    if p1 not in choice:
        print("Unknown move selected, try again.")
        return move()
    global p2
    p2 = input("Player 2. Choose your weapon: ")
    if p2 not in choice:
        print("Unknown move selected, try again.")
        return move()
    else:
        print()
def compare(): # Compares moves to check for a winner.
    if choice.index(p2) == (choice.index(p1) + 1) %3:
        print("Player 1 wins!\n")
        print("**Scoreboard**")
        global P1
        P1 += 1
        score()
    elif choice.index(p2) == (choice.index(p1) + 2) %3:
        print("Player 2 wins!\n")
        print("**Scoreboard**")
        global P2
        P2+= 1
        score()
    elif choice.index(p2) == (choice.index(p1)):
        print("It's a draw!")
        score()
def restart(): # Asks player if they want to play another round
    r = 0
    while r == 0:
        restart = input("\nWould you like to play another round?\n")
        if restart == "yes" or restart == "Yes":
            r = 1
            game()
        else:
            end = input("Enter 'x' to end game:\n")
            print()
            if end == "x" or end == "X":
                r = 1
                print("The game has officially ended.\n")
                if P1 < P2:
                    print("**Congratulations to Player 2 for winning the game!**\n")
                    print("Thank you for playing at Ray's Boom Boom Room. Hope you enjoyed your stay!")
                elif P1 > P2:
                    print("**Congratulations to Player 1 for winning game!**\n")
                    print("Thank you for playing at Ray's Boom Boom Room. Hope you enjoyed your stay!")

                elif P1 == P2:
                    print("**Congratulations to all players, the game has ended in a tie!**\n")
                    print("Thank you for playing at Ray's Boom Boom Room. Hope you enjoyed your stay!")
start()
