# 1. arithmetic calculation program

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# sumNumber = a + b

# try:
#     print(quotient = a / b)
# except ZeroDivisionError:
#     print("Number cannot be divided by Zero")


# 2. Second example using the else and finally clause

# try:
#     number = int(input("Enter a number: "))

# except ValueError:
#     print("Invalid input.")

# else:
#     print(f"You entered {number}.")

# finally:
#     print("Program finished.")

# 3. Rasing an exception
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
