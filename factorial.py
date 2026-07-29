# دریافت عدد از کاربر
number = int(input("Enter a positive integer: "))

# مقدار اولیه فاکتوریل
factorial = 1

# محاسبه فاکتوریل با حلقه
for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of {number} is: {factorial}")
