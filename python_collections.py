print("=" * 50)
print("LIST EXAMPLES")
print("=" * 50)

# Create List
fruits = ["apple", "banana", "orange", "kiwi"]

print("Original List:", fruits)

# 1. append()
fruits.append("mango")
print("append():", fruits)

# 2. insert()
fruits.insert(1, "grape")
print("insert():", fruits)

# 3. extend()
fruits.extend(["pear", "peach"])
print("extend():", fruits)

# 4. remove()
fruits.remove("banana")
print("remove():", fruits)

# 5. pop()
removed = fruits.pop()
print("pop():", removed)
print(fruits)

# 6. index()
print("index('orange'):", fruits.index("orange"))

# 7. count()
fruits.append("apple")
print("count('apple'):", fruits.count("apple"))

# 8. sort()
fruits.sort()
print("sort():", fruits)

# 9. reverse()
fruits.reverse()
print("reverse():", fruits)

# 10. copy()
copy_list = fruits.copy()
print("copy():", copy_list)

# 11. clear()
temp = ["A", "B", "C"]
temp.clear()
print("clear():", temp)

# 12. len()
print("len():", len(fruits))

# 13. in
print("'apple' in fruits:", "apple" in fruits)

# 14. slicing
print("slice [1:4]:", fruits[1:4])

# 15. loop
print("Loop through list:")
for item in fruits:
    print(item)

# --------------------------------------------------------------------------------

print("\n" + "=" * 50)
print("TUPLE EXAMPLES")
print("=" * 50)

numbers = (10, 20, 30, 40, 50, 30)

print("Original Tuple:", numbers)

# 1. count()
print("count(30):", numbers.count(30))

# 2. index()
print("index(40):", numbers.index(40))

# 3. len()
print("len():", len(numbers))

# 4. max()
print("max():", max(numbers))

# 5. min()
print("min():", min(numbers))

# 6. sum()
print("sum():", sum(numbers))

# 7. slicing
print("slice:", numbers[1:4])

# 8. membership
print("20 in tuple:", 20 in numbers)

# 9. iteration
for num in numbers:
    print(num)

# 10. tuple()
new_tuple = (1, 2, 3)
print("tuple():", new_tuple)

# --------------------------------------------------------------------------------

print("\n" + "=" * 50)
print("SET EXAMPLES")
print("=" * 50)

colors = {"red", "green", "blue"}

print("Original Set:", colors)

# 1. add()
colors.add("yellow")
print(colors)

# 2. update()
colors.update(["black", "white"])
print(colors)

# 3. remove()
colors.remove("green")
print(colors)

# 4. discard()
colors.discard("pink")
print(colors)

# 5. pop()
item = colors.pop()
print("pop():", item)

# 6. copy()
copy_set = colors.copy()
print(copy_set)

# 7. union()
print(colors.union({"orange"}))

# 8. intersection()
print(colors.intersection({"red", "orange"}))

# 9. difference()
print(colors.difference({"red"}))

# 10. issubset()
print({"red"}.issubset(colors))

# 11. issuperset()
print(colors.issuperset({"red"}))

# 12. len()
print(len(colors))

# --------------------------------------------------------------------------------

print("\n" + "=" * 50)
print("DICTIONARY EXAMPLES")
print("=" * 50)

student = {"name": "Ali", "age": 22, "city": "Tehran"}

print(student)

# 1. get()
print(student.get("name"))

# 2. keys()
print(student.keys())

# 3. values()
print(student.values())

# 4. items()
print(student.items())

# 5. update()
student.update({"age": 23})
print(student)

# 6. pop()
student.pop("city")
print(student)

# 7. setdefault()
student.setdefault("grade", 20)
print(student)

# 8. copy()
copy_dict = student.copy()
print(copy_dict)

# 9. len()
print(len(student))

# 10. in
print("name" in student)

# 11. clear()
temp = {"A": 1}
temp.clear()
print(temp)

# 12. loop keys
for key in student:
    print(key)

# 13. loop values
for value in student.values():
    print(value)

# 14. loop items
for key, value in student.items():
    print(key, value)

# 15. del
student["country"] = "Iran"
del student["country"]
print(student)

# --------------------------------------------------------------------------------
