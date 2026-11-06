# Student Management System

students = []


def display_menu():
    """Display the main menu."""
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Result")
    print("5. Exit")


def get_number(message):
    """Get a valid number from the user."""
    while True:
        try:
            number = float(input(message))

            if number < 0 or number > 100:
                print("Please enter a number from 0 to 100.")
            else:
                return number

        except ValueError:
            print("Please enter a valid number.")


def add_student():
    """Add a new student."""
    print("\n--- Add Student ---")

    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    age = input("Enter student age: ").strip()

    if age == "":
        print("Student age cannot be empty.")
        return

    try:
        age = int(age)

        if age <= 0:
            print("Age must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid age.")
        return

    mathematics = get_number("Enter Mathematics mark: ")
    english = get_number("Enter English mark: ")
    science = get_number("Enter Science mark: ")

    student = {
        "name": name,
        "age": age,
        "mathematics": mathematics,
        "english": english,
        "science": science
    }

    students.append(student)

    print("Student added successfully.")


def view_students():
    """Display all students."""
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No students found.")
        return

    for number, student in enumerate(students, start=1):
        print(f"\nStudent {number}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Mathematics: {student['mathematics']}")
        print(f"English: {student['english']}")
        print(f"Science: {student['science']}")


def search_student():
    """Search for a student by name."""
    print("\n--- Search Student ---")

    if len(students) == 0:
        print("No students found.")
        return

    search_name = input("Enter student name: ").strip().lower()

    found = False

    for student in students:
        if student["name"].lower() == search_name:
            print("\nStudent found")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Mathematics: {student['mathematics']}")
            print(f"English: {student['english']}")
            print(f"Science: {student['science']}")

            found = True

    if found == False:
        print("Student not found.")


def calculate_result():
    """Calculate the total, average, and grade of a student."""
    print("\n--- Calculate Result ---")

    if len(students) == 0:
        print("No students found.")
        return

    search_name = input("Enter student name: ").strip().lower()

    for student in students:
        if student["name"].lower() == search_name:
            total = (
                student["mathematics"]
                + student["english"]
                + student["science"]
            )

            average = total / 3

            if average >= 70:
                grade = "A"
            elif average >= 60:
                grade = "B"
            elif average >= 50:
                grade = "C"
            elif average >= 40:
                grade = "D"
            else:
                grade = "F"

            print(f"\nResult for {student['name']}")
            print(f"Total: {total}")
            print(f"Average: {average:.2f}")
            print(f"Grade: {grade}")

            return

    print("Student not found.")


def main():
    """Run the Student Management System."""
    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            calculate_result()

        elif choice == "5":
            print("Thank you for using the Student Management System.")
            break

        else:
            print("Invalid choice. Please choose from 1 to 5.")


main()