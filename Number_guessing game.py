import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    guess = int(input("Guess the number between (1, 100): "))
    attempts += 1
    if guess == secret_number:
        print("You Won!")
        break
    else:
        print(f"Wrong guess! Attempts left: {max_attempts - attempts}")

        if attempts == max_attempts and guess != secret_number:
            print(f"Game over! The secret number was {secret_number}")



