from art import *

valid_input = ['+', '-', '*', '/']
prog_end = False
calc_number = None

def add(num1, num2):
    return float(num1 + num2)
def subtract(num1, num2):
    return float(num1 - num2)
def multiply(num1, num2):
    return float(num1 * num2)
def divide(num1, num2):
    return float(num1 / num2)

print(logo)
first_num = float(input("Whats the first number? "))
while(not prog_end):

    operation = input("+\n-\n*\n/\n Pick an opperation: ")
    next_num = float(input("Whats the next number? "))


    if(operation == '+'):
        calc_number = add(first_num, next_num)
        print(f"{first_num} + {next_num} = {calc_number}")
    if(operation == '-'):
        calc_number = subtract(first_num, next_num)
        print(f"{first_num} - {next_num} = {calc_number}")
    if(operation == '*'):
        calc_number = multiply(first_num, next_num)
        print(f"{first_num} * {next_num} = {calc_number}")
    if(operation == '/'):
        calc_number = divide(first_num, next_num)
        print(f"{first_num} / {next_num} = {calc_number}")
    if(operation not in valid_input):
        print("Invalid Operation. Please try again")

    continue_calc = input(f"Type 'y' to continue calculating with {calc_number}, or type 'n' to start a new calcuation: ")

    if(continue_calc == 'y'):
        first_num = calc_number
    if(continue_calc == 'n'):
        prog_end = True
    
    