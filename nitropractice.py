import tkinter as tk
from random import randrange
import math
import time
from tkinter import ttk

window = tk.Tk()

window.configure(background='black')

#Code goes in here

welcome = tk.Label(text="Welcome to NitroPractice - an innovational app to help practice math quickly!",foreground='white',background='black')
problem = tk.Label(foreground='white',background='black')
result = tk.Label(foreground='white',background='black')
score = tk.Label(text="Score: 0", foreground='white',background='black')
enter = tk.Label(text="Enter here:",foreground='white',background='black')

welcome.pack()
problem.pack()
result.pack()
score.pack()
enter.place(x=500,y=140)

def makeQuestion(score_count):
    global operation
    global first_num
    global second_num

    if score_count < 5:
        p_choice = ['addition-1d', 'subtraction-1d']
        problem_select = randrange(2)

        operation = p_choice[problem_select]

        first_num = randrange(10)
        second_num = randrange(10)

        if problem_select == 0:
            return str(first_num) + " + " + str(second_num)
        else:
            if first_num >= second_num:
                return str(first_num) + " - " + str(second_num)
            else:
                return str(second_num) + " - " + str(first_num)
    
    elif score_count < 10:
        p_choice = ['addition-2d','subtraction-2d']
        problem_select = randrange(2)

        operation = p_choice[problem_select]

        first_num = randrange(100)
        second_num = randrange(100)

        if problem_select == 0:
            return str(first_num) + " + " + str(second_num)
        else:
            if first_num >= second_num:
                return str(first_num) + " - " + str(second_num)
            else:
                return str(second_num) + " - " + str(first_num)
    
    elif score_count < 15:
        p_choice = ['addition-3d','subtraction-3d']
        problem_select = randrange(2)

        first_num = randrange(1000)
        second_num = randrange(1000)

        if problem_select == 0:
            return str(first_num) + " + " + str(second_num)
        else:
            if first_num >= second_num:
                return str(first_num) + " - " + str(second_num)
            else:
                return str(second_num) + " - " + str(first_num)
    
    elif score_count < 25:
        first_num = randrange(13)
        second_num = randrange(13)

        operation = 'Basic multiplication'

        return str(first_num) + " x " + str(second_num)
    
    else:
        first_num = randrange(50)
        second_num = randrange(50)

        operation = 'Advanced multiplication'

        return str(first_num) + " x " + str(second_num)

def getAnswer(n1,n2,op):
    if op == "addition-1d" or op == 'addition-2d' or op == 'addition-3d':
        return n1 + n2
    
    elif op == "subtraction-1d" or op == 'subtraction-2d' or op == 'subtraction-3d':
        if n1 >= n2:
            return n1 - n2
        else:
            return n2 - n1
    
    elif op == 'Basic Multiplication' or op == "Advanced Multiplication":
        return n1 * n2

def startGame():

    global score_counter
    score_counter = 0
    
    welcome['text'] = ""
    start_button.pack_forget()

    problem['text'] = makeQuestion(0)

def checkProblem(event):

    global score_counter

    user_ans = user_result.get()

    right_ans = getAnswer(first_num,second_num,operation)


    if int(user_ans) == right_ans:
        score_counter = score_counter + 1

        result['text'] = 'Correct!'
        score['text'] = 'Score: ' + str(score_counter)
    
    else:
        result['text'] = 'Incorrect'

        score_counter = score_counter - 1

        score['text'] = 'Score: ' + str(score_counter)   
    
    problem['text'] = makeQuestion(score_counter)


start_button = tk.Button(text="Click here to start!",command=startGame)
check_next_problem_button = tk.Button(text="Check answer!", command=checkProblem)

window.bind('<Return>', checkProblem)


user_result = tk.Entry(window,width=20)

start_button.pack()
check_next_problem_button.pack()

user_result.pack()

window.mainloop()