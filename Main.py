# Will use tkinter when ready to make GUI for game
# import tkinter as tk;

#TODO Create Game Loop: menu letting user determine what they want to do (Play game, See Past Games, etc)
#TODO Add Different Difficulties: How many problems, how many numbers, What kind of operators
#TODO Plan out GUI screens 
#TODO Make the GUI for the game

import random
import time

class Game:

    # Initializes an instance of a game 
    def __init__(self, problems):
        self.NUM_PROBLEMS = problems
        self.operations = ['+', '-', '*', "%"]
        self.num_incorrect = 0
        self.start_time = None
        self.end_time = None
        self.history = ""

    # Getter Method: Retuns the number of incorrect answers a player had in the game
    def get_num_incorrect(self):
            return self.num_incorrect
    
    # Getter Method: Retuns the number of problems this game has
    def get_num_problems(self):
            return self.NUM_PROBLEMS
    
    # Getter Method: Returns how long it took the user to complete this game
    def get_time(self):
         return self.end_time - self.start_time
    
    # Getter Method: Retuns the documented history of the game (Each problem and answer user had)
    def get_history(self):
         return self.history
    
    # Used to make user play a game
    def play_game(self):
        self.start_time = time.time()
        problem_num = 1
        while problem_num <= self.NUM_PROBLEMS:
            equation, answer = self.gen_equation()
            while True:
                problem = "Problem " + str(problem_num) + ": " + equation + " = "
                response = input(problem)
                self.history += problem + response + "\n"
                try:
                    if(int(response) == answer):
                        break
                    else:
                        self.num_incorrect += 1
                except ValueError: # User inputs an answer that is not a number
                    self.num_incorrect += 1

            problem_num += 1
        self.end_time = time.time()

    # Used to generate equations for current game
    def gen_equation(self):
        operator = self.operations[random.randint(0,3)] # Creates randon number from 0 to 3 inclusive
        num1 = random.randint(1, 20) 
        num2 = random.randint(1, 20)
        equation = str(num1) + " " + operator + " " + str(num2)
        return equation, eval(equation) # Returns the equation in String form and answer to equation in int form


## DRIVER CODE ##

game1 = Game(problems=1)
game1.play_game()

print(f"Total elapsed time: {(game1.get_time()):.3f} seconds")
num_problems = str(game1.get_num_problems())
num_incorrect = str(game1.get_num_incorrect())
print("Out of " + num_problems + (" problem," if int(num_problems) == 1 else " problems,")  + 
      " you answered incorrectly " + num_incorrect + (" time!" if int(num_incorrect) == 1 else " times!"))
print("\nGame History:")
print(game1.get_history())