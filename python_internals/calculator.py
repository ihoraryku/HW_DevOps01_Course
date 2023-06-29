print("Welcome to the Calculator Program! \n")


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
    if operator == "1":
        operator = "+"
    elif operator == "2":
        operator = "-"
    elif operator == "3":
        operator = "*"
    elif operator == "4":
        operator = "/"
    else:
        print("Invalid choice. Please try again.")
        return

    if operator == "/" and num2 == 0:
        print("Error: Cannot divide by zero.")
        return

    if operator == "+":
        result = num1 + num2
        print("The result of addition is:", result)
    elif operator == "-":
        result = num1 - num2
        print("The result of subtraction is:", result)
    elif operator == "*":
        result = num1 * num2
        print("The result of multiplication is:", result)
    elif operator == "/":
        result = num1 / num2
        print("The result of division is:", result)


calculate()
