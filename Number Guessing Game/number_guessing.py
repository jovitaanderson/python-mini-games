import time


# Method to  start game
def start_game():
    print("I will give you 3 seconds to think of a number between 1-1000")
    for i in range(0, 3):
        print(i+1, end=", ")
        time.sleep(1)

    low = 1
    high = 1000
    num_tries = 0
    # Uses binary search to efficiently find the answer
    while low <= high:
        mid = int(low + (high - low) / 2)
        ans = input(f"Is the number {mid}? \n Enter: 'y' for yes, 'h' for higher, 'l' for lower ")
        if ans.lower() not in "yhl":
            print("Invalid input, please type a valid input.")
            continue
        else:
            if ans.lower() == "y":
                print(f"Yay! I guessed it within {num_tries} tries!")
                return True
            elif ans.lower() == "h":
                num_tries += 1
                low = mid + 1
            elif ans.lower() == "l":
                num_tries += 1
                high = mid - 1
    return False


# Method to play game again
def play_again():
    successful = start_game()
    if successful:
        print("Do you want to play again? :)")
    else:
        print("You may have answered the question wrongly :(, do you want to try again?")

    again = input("Type y to continue, and any other character to quit ")
    if again == "y":
        play_again()
    else:
        print("Thank you for playing!")


def main():
    # print title of game
    print("===========================")
    print("|| Number guessing game! ||")
    print("===========================")
    # print instructions of game
    print("How to play: ")
    print("Think of a whole number between 1-1000 inclusive and the computer", end=" ")
    print("will try and guess your number within 10 tries!")
    print("Each round the computer will guess a number and ask if the number is correct,", end=" ")
    print("higher or lower and you will have to answer accordingly")
    time.sleep(2)
    input("Are you ready? Press enter to continue. ")
    play_again()


# Driver code to start game
main()
