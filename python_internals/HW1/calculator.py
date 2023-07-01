
def calculate():
    print("Welcome to the Calculator Program!\n")

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
        print("\nInvalid choice. Please try again.")
        return

    if operator == "/" and num2 == 0:
        print("\nError: Cannot divide by zero.")
        return

    try:
        result = eval(f"{num1} {operator} {num2}")
        print("\nThe result is:", result)
    except ZeroDivisionError:
        print("\nError: Cannot divide by zero.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")


calculate()
