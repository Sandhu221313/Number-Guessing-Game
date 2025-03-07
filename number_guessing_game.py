import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)
print(number_to_guess)  # This will print the number (for testing purposes, you can remove it later)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Difficulty Selection
print("\nPlease select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

difficulty = input("Choose the difficulty level: 1. Easy, 2. Medium, 3. Hard: ").lower()

# Set the number of attempts based on the difficulty level
if difficulty == "1" or difficulty == "easy":
    max_attempts = 10
    print("Great! You have selected the Easy difficulty level.")
elif difficulty == "2" or difficulty == "medium":
    max_attempts = 5
    print("Great! You have selected the Medium difficulty level.")
elif difficulty == "3" or difficulty == "hard":
    max_attempts = 3
    print("Great! You have selected the Hard difficulty level.")
else:
    print("Invalid choice. Defaulting to Medium difficulty.")
    max_attempts = 5  # Default to medium difficulty if invalid input

# Number Guessing Loop
while max_attempts > 0:
    try:
        user_guess = int(input(f"\nYou have {max_attempts} attempts left. Enter your guess: "))

        # Check if the guess is correct
        if user_guess < number_to_guess:
            print(f"Incorrect! The number is greater than {user_guess}.")
        elif user_guess > number_to_guess:
            print(f"Incorrect! The number is less than {user_guess}.")
        else:
            print("🎉 Congratulations! You guessed the correct number!")
            break  # Exit the loop if the guess is correct

        max_attempts -= 1  # Reduce attempts after each guess

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Game Over if no attempts left
if max_attempts == 0:
    print(f"\nOut of attempts! The correct number was {number_to_guess}. Better luck next time! 😊")
