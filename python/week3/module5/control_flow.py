# IF STATEMENT
# SYNTAX

"""
declare variable
if condition:
    # statement to execute if condition is True
"""

# age = 18
# if age >= 18:
#     print("You are an adult.")

# if-elif
# Syntax
"""
declare variable
if contdition1:
    # statement to execute if condition1 is True
elif condition2:
    # statement to execute if condition2 is True
"""

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Eligible!! You are an adult.")

# elif age < 18 and age > 0:
#     print("Not Eligible!! You are a minor.")

# elif age == 0:
#     print("You are a newborn.")

# else:
#     print("Invalid age entered.")


# Loops

# For Loop
# Syntax:
"""
for variable in iterable:
    # statement to execute for each item in the iterable
"""

# for numbers in range(1,11):
#     print(numbers)


# # iterating through a list
# students = ["John", "Mary", "David"]

# for student in students:
#     print(student)

# # iterating throgh a string
# word = "Python"

# for character in word:
#     print(character)

# WHILE LOOP
# Syntax:
"""
while condition:
    # statement to execute while condition is True
"""

age = 10

while age < 18:
    print("You are minor.")
    age += 1