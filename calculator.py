"""
calculator.py

A simple command-line calculator with error handling.

"""

# -----------------------------
# Calculator Functions
# -----------------------------


def add(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2


def subtract(num1, num2):
    """Return the subtraction of two numbers."""
    return num1 - num2


def multiply(num1, num2):
    """Return the multiplication of two numbers."""
    return num1 * num2


def divide(num1, num2):
    """
    Return the division of two numbers.

    Raises:
        ZeroDivisionError: If num2 is zero.
    """
    if num2 == 0:
        raise ZeroDivisionError

    return num1 / num2


# -----------------------------
# Helper Functions
# -----------------------------


def show_menu():
    """Display calculator menu."""

    print("\n" + "=" * 45)
    print("         PYTHON CALCULATOR")
    print("=" * 45)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("=" * 45)


def get_number(message):
    """
    Get a valid number from the user.
    """

    while True:
        try:
            number = float(input(message))
            return number

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def get_choice():
    """
    Get a valid menu choice.
    """

    while True:
        choice = input("Choose an option (1-5): ").strip()

        if choice in ("1", "2", "3", "4", "5"):
            return choice

        print("❌ Please choose a number between 1 and 5.")


def ask_again():
    """
    Ask the user if they want another calculation.
    """

    while True:
        answer = input("\nDo you want another calculation? (y/n): ").strip().lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print("❌ Please enter y or n.")


# -----------------------------
# Main Program
# -----------------------------


def main():

    print("Welcome to Python Calculator!")

    while True:

        show_menu()

        choice = get_choice()

        if choice == "5":
            print("\nThank you for using the calculator.")
            print("Goodbye!")
            break

        number1 = get_number("Enter the first number: ")
        number2 = get_number("Enter the second number: ")

        try:

            if choice == "1":
                result = add(number1, number2)
                operation = "+"

            elif choice == "2":
                result = subtract(number1, number2)
                operation = "-"

            elif choice == "3":
                result = multiply(number1, number2)
                operation = "*"

            else:
                result = divide(number1, number2)
                operation = "/"

            print(f"\nResult: {number1} {operation} {number2} = {result}")

        except ZeroDivisionError:
            print("\n❌ Error: Division by zero is not allowed.")

        if not ask_again():
            print("\nThank you for using the calculator.")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()