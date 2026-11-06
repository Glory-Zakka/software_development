# Data structures in python

# 1. Lists
# Lists are ordered collections of items that can be of different types. They are mutable, meaning

# syntax:
"""
list_name = [list1, list2, list3, ...]
"""

# python_students = ["Suleiman", "Elijah", "Sadiq", "Lawal"]
# # print(python_students)

# # Operations on lists
# # 1. Accessing elements in a list
# print(python_students[2])
# print(python_students[-1])
# print(python_students[-4])

# # 2. Modifying elements in a list

# # modify the third element in the list
# python_students[2] = "Sadeeq"

# # print the modified list
# print(python_students)

# # 3. Adding elements to a list
# # append() method adds an element to the end of the list
# python_students.append("Aisha")
# print(python_students)

# # 4. Removing elements from a list
# # remove() method removes the first occurrence of an element from the list
# python_students.remove("Elijah")
# print(python_students)


# 2. Tuples
# Tuples are ordered collections of items that can be of different types. They are immutable,
# Syntax:

"""
tuple_name = (item1, item2, item3, ...)"""


# shopping_items = ("Meat", "Rice", "Beans", "Vegetables")
# print(shopping_items)

# Dictionaries
# Dictionaries are unordered collections of key-value pairs. They are mutable, meaning you can change their
# Syntax:

"""
dictionary_name = {key1: value1, key2: value2, key3: value3, ...}

"""

student_info = {
    "name": "Suleiman",
    "age": 20,
    "course": "Computer Science",
    "Lga": "Bauchi"
}

print(student_info)

# operations on dictionaries
# 1. Accessing values in a dictionary
print(student_info["name"])
print(student_info["age"])
print(student_info["course"])
print(student_info["Lga"])  

# 2. Modifying values in a dictionary
student_info["age"] = 30
print(student_info)

# 3. Adding key-value pairs to a dictionary
student_info["state"] = "Bauchi"
print(student_info)

# 4. Removing key-value pairs from a dictionary
del student_info["state"]
print(student_info)


# Sets
# Sets are unordered collections of unique items. They are mutable, meaning you can change their contents

# syntax:

"""
set_name = {set1, set2, set3, ...}
"""

# skills = {"Python", "Java", "C++", "JavaScript", "Python"}
# print(skills)

# skills.add("Docker")
# skills.remove("Java")
# print(skills)


backend = {"Python", "SQL", "Git"}
data = {"Python", "SQL", "Pandas"}

print(backend | data)  # union
print(backend & data)  # intersection
print(data - backend)  # difference
