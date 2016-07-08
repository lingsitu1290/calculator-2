"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

continue_on  = True

while continue_on == True: 


    # Your code goes here
    calculate = raw_input("Please name the operand(+ - * / square cube pow mod) followed by the numbers.")

    tokens = calculate.split(" ")

    if len (tokens) >= 2:
        num1 = int(tokens[1])
    if len(tokens) == 3:
        num2 = int(tokens[2])
    #print input_string

    if tokens[0] == '+':
        print add(num1, num2)

    elif tokens[0] == '-':
        print subtract(num1, num2)

    elif tokens[0] == '*':
        print multiply(num1, num2)

    elif tokens[0] == '/':
        print num1, num2
        print divide(num1, num2)

    elif tokens[0] == 'square':
        print square(num1)

    elif tokens[0] == 'cube':
        print cube(num1)

    elif tokens[0] == 'pow':
        print power(num1, num2)

    elif tokens[0] == 'mod':
        print mod(num1, num2)

    elif tokens[0] == 'q':
        print "Goodbye"
        continue_on = False

    else:
        print "You must have made error"



