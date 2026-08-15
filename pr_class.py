students = []
products = []


class Student:
    def __init__(self, name, age, student_id, major, grade):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.major = major
        self.grade = grade

    def add(self):
        students.append(self.__dict__)

    def remove(self, student_id):
        for student in students:
            if student["student_id"] == student_id:
                students.remove(student)
                break

    def show(self):
        print(students)


class Product:
    def __init__(self, name, price, product_id, category, stock):
        self.name = name
        self.price = price
        self.product_id = product_id
        self.category = category
        self.stock = stock

    def add(self):
        products.append(self.__dict__)

    def remove(self, product_id):
        for product in products:
            if product["product_id"] == product_id:
                products.remove(product)
                break

    def show(self):
        print(products)


s1 = Student("Ali", 20, 1, "Computer", 18)
s1.add()

s2 = Student("Reza", 21, 2, "IT", 17)
s2.add()

s1.remove(1)
s1.show()


p1 = Product("Laptop", 500, 101, "Digital", 10)
p1.add()

p2 = Product("Mouse", 20, 102, "Accessory", 25)
p2.add()

p1.remove(101)
p1.show()
