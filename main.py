import random

play = "y"

while play == "y":

    print("\nChoose difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    difficulty = input("Enter your choice (1/2/3): ")

    if difficulty == "1":
        max_number = 50
    elif difficulty == "2":
        max_number = 100
    elif difficulty == "3":
        max_number = 200
    else:
        print("Invalid choice! Starting with Medium difficulty.")
        max_number = 100

    # Computer selects a random number
    number = random.randint(1, max_number)

    print("\n🎯 Welcome to the Awesome Number Guessing Game! 🎯")
    print(f"Guess a number between 1 and {max_number}")

    guess = 0
    attempts = 0

    # Loop until the user guesses correctly
    while guess != number:

        guess = int(input("Guess a number: "))
        attempts += 1

        if guess < 1 or guess > max_number:
            print(f"Please enter a number between 1 and {max_number}.")
        elif guess > number:
            print("TOO HIGH! Try again.")
        elif guess < number:
            print("TOO LOW! Try again.")
        else:
            print(f"CONGRATULATIONS! 🎉 You guessed the number in {attempts} attempts!")

    play = input("\nDo you want to play again? (y/n): ").lower()

print("Thanks for playing! 🎮")
