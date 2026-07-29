print("*" * 50)
print("Student Information")
print("*" * 50)

# Create Dictionary
student = {
    "first_name": "Abolfazl",
    "last_name": "Ghafouri",
    "age": 25,
    "university": "Islamic Azad University",
    "major": "Computer Engineering",
}

# Print specific values
print("\nStudent Name:")
print(student["first_name"], student["last_name"])

print("\nUniversity:")
print(student["university"])

print("\nMajor:")
print(student["major"])

# Print all information using for loop
print("\nAll Student Information:")

for key, value in student.items():
    print(f"{key}: {value}")
