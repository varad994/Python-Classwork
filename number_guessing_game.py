
import random

number_to_guess = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
