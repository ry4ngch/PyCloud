import random
import os
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

game_on = True

def start_game():
    clear()
    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty [Easy/Hard]: ").lower()
    attempts = 0
    pick_number = random.randint(1, 100)
    end_game = False

    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    while attempts > 0 and not end_game:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess_number = int(input("Make a guess: "))
        if guess_number == pick_number:
            print(f"You got it! The number was {guess_number}")
            end_game = True
        elif guess_number > pick_number:
            print("Number too high")
        else:
            print("Number too low")
        attempts -= 1

while game_on:
    start_game()
    game_on = input("Do you want to restart the game? [y/n]: ").lower() == "y"
