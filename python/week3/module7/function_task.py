"""
Task1:
Write a function that asks for three scores of a student, 
calculates an average, assigns a grade and prints the result.
"""

# program for the above task

def user_grades():
    score1 = float(input("Enter your score: "))
    score2 = float(input("Enter your score: "))
    score3 = float(input("Enter your score: "))

    average = (score1 + score2 + score3)/3

    if average >=70:
        print("Grade A")
    elif average >=50 and average < 70:
        print("Grade B") 
    elif average >=40 and average < 50:
        print("Grade C")
    else:
        print("Carry over student")

user_grades()


