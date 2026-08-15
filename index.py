# file = open("file.txt", "w") 
# file.write("Hi Hi")
# file.close()

# file = open("file.txt", "a") 
# file.write("\nbye bye")
# file.close()

# file = open("file.txt", "r")  
# print(file.read())
# file.close()

with open("file.txt", "w") as file:
    file.write("Hi Hi")

with open("file.txt", "a") as file:
    file.write("\nbye bye")

with open("file.txt", "r") as file:
    print(file.read())
