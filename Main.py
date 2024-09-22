# Will use tkinter when ready to make GUI for game
# import tkinter as tk;

#TODO Add stats: number of wrong asnwers and time
#TODO Add different difficulties: How many problems, how many numbers, What kind of operators
#TODO Plan out GUI screens 
#TODO Make the GUI for the game

import random

opeartions = ['+', '-', '*', "%"]

NUM_PROBLEMS = 10
# Generates an equation with 2 numbers and one operator
def gen_equation():
    operator = opeartions[random.randint(0,3)] # Creates randon number from 0 to 3 inclusive
    num1 = random.randint(1, 20) 
    num2 = random.randint(1, 20)
    equation = str(num1) + " " + operator + " " + str(num2)
    return equation, eval(equation) # Returns the equation in String form and answer to equation in int form

problem_num = 0
while problem_num <= NUM_PROBLEMS:
    equation, answer = gen_equation()
    while True:
        response = input("Problem " + str(problem_num) + ": " + equation + " = ")
        if(int(response) == answer):
            break
    problem_num += 1

print("Congragulations! You've answered all the problems correctly!")