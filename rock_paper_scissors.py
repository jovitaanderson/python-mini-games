import random

choices = ["rock", "paper", "scissors"]


def player_input():
    move = input("Choose your move: \n 1.Rock \n 2.Paper \n 3.Scissors \n")
    if move in "123":
        results(choices[int(move) - 1])
    else:
        print("Invalid input, try again")
        player_input()


def results(player_choice):
    # get a random choice to fight against player
    random_choice = choices[random.randint(0, len(choices) - 1)]
    if player_choice == random_choice:
        result = f"Both picked {random_choice}, it is a tie"
    elif (player_choice == "rock" and random_choice == "scissors") or (player_choice == "paper" and random_choice == "rock") or (player_choice == "scissors" and random_choice == "paper"):
        result = f"You picked {player_choice}, opponent picked {random_choice}, you win! :)"
    else:
        result = f"You picked {player_choice}, opponent picked {random_choice}, you lose! :("

    print(result)


def main():
    player_input()
    play_again = input("Would you like to player again? Enter y for yes any other char to exit:")
    if play_again == 'y' or play_again == 'Y':
        main()
    print("Thank you for playing!")


main()