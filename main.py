code_melli = input("Enter your national ID (code melli): ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

print(age + age)
print(age * age)
print(age - 10)
print(age / 2)
print(age % 3)
print(age**2)
print(age // 3)
print(age + 5)
print(age - 5)

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
