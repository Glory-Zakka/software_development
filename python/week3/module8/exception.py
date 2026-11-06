"""
Syntax: 
try:
    code structure

except typeofError:
    statement
"""

try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("Please enter a valid number.")
