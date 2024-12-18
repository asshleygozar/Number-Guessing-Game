import random

message = ''' From 1 - 100, guess the number. You only have 3 attempts to try. '''
number = random.randint(1,100)

def guess():
    attempts = 3
    while True:
        user_guess = int(input("Enter your guess: "))
        if attempts == 1:
            print(f"You failed! Correct number: {number}")
            break
        elif user_guess > number:
            print("Too high")
            attempts = attempts - 1
            print(f"Remaining Attempt: {attempts}")
        elif user_guess < number:
            print("Too low")
            attempts = attempts - 1
            print(f"Remaining Attempt: {attempts}")
        else:
            print("Congratulations! You guess it!")
            break

guess()