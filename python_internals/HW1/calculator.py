print("Welcome to the Calculator Program!\n")


def calculate():
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    operator = input(
        """\nPlease select an operation:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division

        Enter your choice (1-4): """
    )

    try:
        operator = {
            "1": "+",
            "2": "-",
            "3": "*",
            "4": "/"
        }[operator]
    except KeyError:
        print("Invalid choice. Please try again.")
        return

    if operator == "/" and num2 == 0:
        print("Error: Cannot divide by zero.")
        return

    try:
        result = eval(f"{num1} {operator} {num2}")
        print("\nThe result is:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


calculate()
