import random

play = "y"

while play == "y":

    # Computer selects a random number between 1 and 100

    number = random.randint(1, 100)

    print("🎯 WELCOME TO THE NUMBER GUESSING GAME 🎯")
    print("Guess a number between 1 and 100")

    guess = 0
    attempts = 0

    # Loop until the user guesses correctly

    while guess != number:
        guess = int(input("Guess a number: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        elif guess > number:
            print("TOO HIGH! Try again.")
        elif guess < number:
            print("TOO LOW! Try again.")
        else:
            print(f"CONGRATULATIONS!🎉 You guessed the number in {attempts} attempts")

    play = input("Do you want to play again? (y/n): ").lower()

print("Thanks for playing‼ 🎮")
