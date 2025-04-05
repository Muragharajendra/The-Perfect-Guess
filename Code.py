import random

# Random number between 1 and 100
number_to_guess = random.randint(1, 100)

user_guess = -1
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?\n")

# Keep asking until the correct number is guessed
while user_guess != number_to_guess:
    
        user_guess = int(input("Enter your guess: "))
        if user_guess > number_to_guess:
            print("Too high! Try a smaller number.\n")
        elif user_guess < number_to_guess:
            print("Too low! Try a larger number.\n")
        attempts += 1

print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
