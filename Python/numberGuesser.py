import random  # Importing the random module to generate random numbers

def guess_the_number():
    print("🎮 Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100...")

    # Step 1: Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Step 2: Initialize the number of attempts
    attempts = 0

    while True:  # Loop until the player guesses the correct number
        try:
            # Step 3: Ask the player for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1  # Count every valid guess
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue  # Skip the rest of the loop and ask again

        # Step 4: Compare the guess with the secret number
        if guess < secret_number:
            print("🔻 Too low! Try again.")
        elif guess > secret_number:
            print("🔺 Too high! Try again.")
        else:
            print(f"✅ Correct! You guessed the number in {attempts} attempts.")
            break  # Exit the loop when guessed correctly

# Step 5: Run the game
guess_the_number()
