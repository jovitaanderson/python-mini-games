import random
import time

choices = ["rock", "paper", "scissors"]


# Once player input is valid, the results' method is called
def player_input():
    move = input("Choose your move: \n 1.Rock \n 2.Paper \n 3.Scissors \n")
    if move in "123":
        results(choices[int(move) - 1])
    else:
        print("Invalid input, try again")
        player_input()


# Method to get results from computer against player
def results(player_choice):
    # Get a random choice to fight against player
    random_choice = choices[random.randint(0, len(choices) - 1)]
    # States when player wins the game
    if player_choice == random_choice:
        result = f"Both picked {random_choice}, it is a tie :O"
    elif (player_choice == "rock" and random_choice == "scissors") or (
            player_choice == "paper" and random_choice == "rock") or (
            player_choice == "scissors" and random_choice == "paper"):
        result = f"You picked {player_choice}, opponent picked {random_choice}, you win! :)"
    # If none of the states are true, the player has lost
    else:
        result = f"You picked {player_choice}, opponent picked {random_choice}, you lose! :("

    print(result)


# start method to recursively start game again by calling itself
def start():
    player_input()
    play_again = input("Would you like to player again? Enter y for yes any other char to exit:")
    if play_again == 'y' or play_again == 'Y':
        start()
    else:
        print("Thank you for playing!")


# Method to print out intro of the game
def intro():
    print("================================= ")
    print("|| Rock, paper, scissors game! ||")
    print("================================= ")
    print("How to play: ")
    print("You and the computer fight against each other and will choose one of the following actions")
    print("1.Rock 2. Paper 3.Scissors \nHow to win: Rock beats Scissors, Scissors beats Paper, Paper beat Rock")
    time.sleep(2)
    print("Are you ready? Lets go in ...")
    for i in range(0, 3):
        time.sleep(1)
        print(f"{i + 1}, ", end="")

    start()


# Driver code to start game
intro()

