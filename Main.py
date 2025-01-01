import random
import math

class Number_Guessing_Game:

    def __init__(self):

        self.number_of_guessing = 0
        self.generated_random_number = 0
        self.total_number_of_attempts = 0

    def start_game(self):

        while True:

            try:

                print("Welcome to Number Guessing Game!")
                print("Enter your range")

                lower_bound = int(input("Enter lower bounds: "))
                upper_bound = int(input("Enter upper_bounds: "))

                self.generated_random_number = random.randint(lower_bound,upper_bound)
                self.number_of_guessing = round(math.log2(upper_bound - lower_bound + 1))

                print(f"You have only {self.number_of_guessing} attempts to guess the number. Good Luck!")

                number_guessing_game.guessing_game()

                break

            except ValueError:

                print("Integer only!")

    def guessing_game(self):
        
        while True:

            try:
                user_input = int(input("Enter your Guess: "))

                if user_input > self.generated_random_number:

                    print("Your guess is too high! Try again")
                    self.number_of_guessing -= 1
                    self.total_number_of_attempts +=1

                    if self.number_of_guessing == 0:

                         print("You've used all of your chances. Better luck next time!")
                         print(f"Correct number: {self.generated_random_number}")
                         break

                elif user_input < self.generated_random_number:

                    print("Your guess is too low! Try again")
                    self.number_of_guessing -= 1
                    self.total_number_of_attempts +=1

                    if self.number_of_guessing == 0:

                         print("You've used all of your chances. Better luck next time!")
                         print(f"Correct number: {self.generated_random_number}")
                         break

                else:
                    print(f"Congratulations! You guessed it within {self.total_number_of_attempts} attempts")
                    break

            except ValueError:

                print("Integer Number Only!")

number_guessing_game = Number_Guessing_Game()
number_guessing_game.start_game()  
        





