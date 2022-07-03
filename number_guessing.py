import time


def start_game():
    print("I will give you 3 seconds to think of a number between 1-1000")
    for i in range(0,3):
        print(i+1, end=", ")
        time.sleep(1)

    low = 1
    high = 1000
    num_tries = 0
    while low <= high:
        mid = int(low + (high - low) / 2)
        ans = input(f"Is the number {mid}? \n Enter: 'y' for yes, 'h' for no, it is higher, 'l' for no, it is lower ")
        if ans.lower() not in "yhl":
            print("Invalid input, please type a valid input.")
            continue
        else:
            if ans.lower() == "y":
                print(f"Yay! I guessed it within {num_tries} of tries!")
                return True
                break
            elif ans.lower() == "h":
                num_tries += 1
                low = mid + 1
            elif ans.lower() == "l":
                num_tries += 1
                high = mid - 1
    return False


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
    print("Welcome to the number guessing game! \nHow to play: ")
    print("Think of a whole number between 1-1000 inclusive, and the computer will guess your number within 10 tries!")
    print("The computer will ask if the guessed number is correct, higher or lower and you will have to answer correctly")
    time.sleep(2)
    var = input("Enter any char to start the game ")
    play_again()
