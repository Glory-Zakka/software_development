def get_positive_number():

    while True:
        try:
            user_input = float(input("Please enter a number: "))

        # valiidate user input
            if user_input > 0:
                return user_input
            else:
                print("Error! The number must be greater than 0")

        except ValueError:
          print("Error! Please enter an integer")


print(get_positive_number())