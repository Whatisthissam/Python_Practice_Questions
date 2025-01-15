import random

random_number = random.randint(1, 10)

guess = int(input("Guess the number between 1 and 10: "))

while guess != random_number:
    print("Wrong guess, try again!")
    guess = int(input("Guess the number between 1 and 10: "))

print(f"Congratulations! You guessed the correct number: {random_number}")
