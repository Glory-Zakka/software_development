import calculator

print(calculator.add(5, 6))

# subtract function from the calculator module
print(calculator.subtract(7,5))

print(calculator.product(5, 5))

print(calculator.quotient(10, 5))



# For importing specific functions from the module
from calculator import add

print(add(5,10))