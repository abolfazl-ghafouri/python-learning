class Person:
    def __init__(self, name, age, national_id, phone, address):
        self.name = name
        self.age = age
        self.national_id = national_id
        self.phone = phone
        self.address = address

    def add(self):
        pass

    def remove(self):
        pass

    def show(self):
        pass


class Student(Person):
    def __init__(
        self,
        name="",
        age="",
        national_id="",
        phone="",
        address="",
        student_id="",
        major="",
        grade="",
    ):
        super().__init__(name, age, national_id, phone, address)
        self.student_id = student_id
        self.major = major
        self.grade = grade

    def add(self):
        with open("students.txt", "a") as file:
            file.write(
                f"{self.name}|{self.age}|{self.national_id}|"
                f"{self.phone}|{self.address}|{self.student_id}|"
                f"{self.major}|{self.grade}\n"
            )

    def remove(self):
        student_id = get_input("Student ID: ")

        with open("students.txt", "r") as file:
            students = file.readlines()

        with open("students.txt", "w") as file:
            for student in students:
                data = student.strip().split("|")

                if data[5] != student_id:
                    file.write(student)

    def show(self):
        with open("students.txt", "r") as file:
            for student in file:
                print(student.strip())


def get_input(message):
    return input(message)


choice = get_input("1. Add Student\n2. Remove Student\n3. Show Students\nChoose: ")

student = Student()

if choice == "1":
    student.name = get_input("Name: ")
    student.age = get_input("Age: ")
    student.national_id = get_input("National ID: ")
    student.phone = get_input("Phone: ")
    student.address = get_input("Address: ")
    student.student_id = get_input("Student ID: ")
    student.major = get_input("Major: ")
    student.grade = get_input("Grade: ")

    student.add()

elif choice == "2":
    student.remove()

elif choice == "3":
    student.show()

else:
    print("Invalid choice")
