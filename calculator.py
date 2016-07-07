"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

input_string  = 'Start'

while input_string[0] != 'False': 


    # Your code goes here
    calculate = raw_input("Please name the operand(+ - * / square cube pow mod) followed by the numbers.")

    input_string = calculate.split(" ")

    #print input_string

    if input_string[0] == '+':
        print add(int(input_string[1]), int(input_string[2]))

    elif input_string[0] == '-':
        print subtract(int(input_string[1]), int(input_string[2]))

    elif input_string[0] == '*':
        print multiply(int(input_string[1]), int(input_string[2]))

    elif input_string[0] == '/':
        print divide(int(input_string[1]), int(input_string[2]))

    elif input_string[0] == 'square':
        print square(int(input_string[1]))

    elif input_string[0] == 'cube':
        print cube(int(input_string[1]))

    elif input_string[0] == 'pow':
        print power(int(input_string[1]), int(input_string[2]))

    elif input_string[0] == 'mod':
        print mod(int(input_string[1]), int(input_string[2]))

    elif input_string[0] == 'q':
        print "Goodbye"
        input_string[0] = 'False'

    else:
        print "You must have made error"



