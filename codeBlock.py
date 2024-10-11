import art
import random


def set_difficulty():
    difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard':")).strip().lower()
    if difficulty == 'easy':
        return 10 # easy mode has 10 attempts
    elif difficulty == 'hard':
        return 5 # hard mode has 5 attempts
    else:
        print("Invalid entry, defaulting to easy mode")
        return 10

def check_guess(guess, answer, attempts_left):
    if guess > answer:
        print("Too high")
        return attempts_left - 1
    elif guess < answer:
        print("Too low")
        return attempts_left - 1
    else:
        print(f"You guessed it! The answer was {answer}")
        return 0 #reset game to zero, since the user guessed the correct answer.

def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game.\n")
    print("I'm thinking of a number between 1 & 50")
    answer = random.randint(1,50)
    attempts_left = set_difficulty()
    guess = None
    while attempts_left > 0 and guess != answer:
        print(f"\nYou have {attempts_left} attempts to guess the correct number.")

        #ask user to make a guess.
        guess = int(input("Make a guess:"))

        #check the guess and adjust the attempts left
        attempts_left = check_guess(guess, answer, attempts_left)

        #User did not guess correctly and ran out of attempts
        if attempts_left == 0 and guess != answer:
            print(f"You ran out of guess. The correct answer was {answer}")

def start_game():
    """Func to start the game"""
    while True:
        play_game()
        play_again = input("Would you like to play again? Type 'Y' or 'N':").lower()
        if play_again == 'n':
            print("Thank you for playing. See you next time.")
            break

#Starting the game
if __name__ == "__main__":
    start_game()