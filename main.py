print("Welcome to the guessing game")
print("You can guess a number between 1 and 10")
print("\nYou have 3 guesses")

secret_number = 6
guess_count = 0
guess_limit = 3
while guess_count < 3:
    guess = int(input(f"Guess {guess_count + guess_limit}: "))
    if guess == secret_number:
        print("You Win!")
        break
    guess_count += 1











