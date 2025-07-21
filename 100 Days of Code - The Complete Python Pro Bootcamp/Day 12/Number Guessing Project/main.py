import art
print(art.logo)
import random as random

number = random.randint(1, 100)

def attempts_for_game(level):
    game_chances = 0
    if level == 'easy':
        game_chances = 10
    elif level == 'hard':
        game_chances = 5
    return game_chances


def make_guess(chances):
    print(f"You have {chances} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    chances -= 1
    if user_guess > number:
        print("Too high")
    elif user_guess < number:
        print("Too low")
    if user_guess == number:
        print(f"You got it! The answer was {number}")
    return user_guess, chances


def game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    guess_left = attempts_for_game(level)
    user_input, guess_left = make_guess(guess_left)
    while guess_left > 0 and user_input != number:
        print("Guess again.")
        user_input, guess_left = make_guess(guess_left)

game()
