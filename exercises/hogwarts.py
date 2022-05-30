# Creating a list of dictionaries.

students = [
    {"name": "Hermione", "house": "Gryffindor", "patrouns": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patrouns": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patrouns": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patrouns": None}
]

for student in students:
    print(student["name"], student["house"], student["patrouns"], sep=', ')

# Creating a dictionary, to create key:value pairs,
# and then using a for loop to itterate over the key:value pairs to print out, the students and their house.
# It first itterates over the key, and then the value which is why you seperate it in the print function to display the value, and then
# Seperate them with the sep method.

''''
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"}

for student in students:
    print(student, students[student], sep=", ")
    
'''

# Working with just list ---

'''
for student in students:
    print(student)
'''

# Using range, and len to go over a list, also using + 1 on i in the range to not show the first item in the list as 0.
'''
for i in range(len(students)):
    print(i + 1, students[i])
'''
