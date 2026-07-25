print("\n=== Fibonacci Sequence ===")

n = int(input("How many Fibonacci numbers do you want? "))

first = 0
second = 1

print("Fibonacci sequence:")

for i in range(n):
    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number

print()
