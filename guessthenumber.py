import random

def game_start():
    global upper_bound
    upper_bound = input("Enter a number to be the upper bound of the interval: ")
    try:
        upper_bound = int(upper_bound)
    except:
        print("Only positive integers!")
        game_start()
    if upper_bound < 0:
        print("Only positive integers!")
        game_start()
    global secret_number
    secret_number = random.randint(0, upper_bound)

def game_main():
    global guess
    guess = input(f"Enter a number between 0 and {upper_bound}: ")
    try:
        guess = int(guess)
    except:
        print(f"Only positive integers less than upper bound: {upper_bound}")

    if guess > upper_bound and guess > 0:
        print(f"Only positive integers less than upper bound {upper_bound}")

    if guess == secret_number:
        print("You found the correct number")
    elif guess > secret_number:
        print("You should go lower.")
        game_main()
    else:
        print("You should go higher.")
        game_main()

def game_replay():
    global restart
    restart = input("Do you want to play again? (Y)es or (N)o: ")
    if restart == "Y":
        game_start()
        game_main()
        game_replay()
    elif restart == "N":
        exit()
    else:
        print("Please enter only Y or N!")

game_start()
game_main()
game_replay()
