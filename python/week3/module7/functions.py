# Defining a function

#Syntax
"""
def function_name(parameters):
    # function body

# calling a function
function_name(arguments)
"""

# default parameters
def greet_user(Username="Elijah"):
    print(f"Hello, welcome to python class {Username}")

greet_user()

#2. parameter arguments
def greet(Username):
    print(f"Hello, welcome to python class {Username}")

greet(
    Username="Elijah"
)


# preferred way to call a function
def welcome(Username):
    print(f"Hello, welcome to python class {Username}")

welcome("Elijah")
welcome("John")
welcome("Lawal")


# Parameters and Arguments
# Example: write a function that takes in two numbers and returns their sum
def add_numbers(number1, number2):
    print(number1 + number2)

add_numbers(5, 10)
