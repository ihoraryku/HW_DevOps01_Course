#!/usr/bin/env python


MAX_ATTEMPTS = 3
DECIMAL_PRECISION = None


def calculate():
    print("Welcome to the Calculator Program!\n")

    num1, num2 = get_numbers()
    operator = get_operator()
    result = perform_operation(num1, num2, operator)
    print_result(result)


def get_numbers():
    def get_float_input(message):
        for attempts in range(MAX_ATTEMPTS):
            try:
                value = float(input(message).replace(',', '.'))
                return value
            except ValueError:
                print("\nInvalid value. Please enter an integer or float number!\n")

        print(f"You entered the wrong value {MAX_ATTEMPTS} times. Please check your initial data and try again later.")
        exit(0)

    num1 = get_float_input("Please enter the first number: ")
    num2 = get_float_input("Please enter the second number: ")
    return num1, num2


def get_operator():
    for attempts in range(MAX_ATTEMPTS):
        try:
            operator = input(
                """\nPlease select an operation:
                1. Addition
                2. Subtraction
                3. Multiplication
                4. Division

                Enter your choice (1-4): """
            )

            operator = {
                "1": "+",
                "2": "-",
                "3": "*",
                "4": "/"
            }[operator]

            return operator

        except KeyError:
            print("\nInvalid choice. Please enter an integer between 1 and 4!")

    print(f"You entered the wrong value {MAX_ATTEMPTS} times. Please check your initial data and try again later.")
    exit(0)


def perform_operation(num1, num2, operator):
    try:
        result = eval(f"{num1} {operator} {num2}")
        return result
    except ZeroDivisionError:
        print("""\n
Error: Cannot divide by zero. When dividing, the second number must not be zero. 
Please enter another second number or select another operation and try again!"""
              )
        return None
    except Exception as error:
        print(f"\nAn error occurred: {str(error)}")
        return None


def print_result(result):
    if result is not None:
        result = format_result(result)
        print("\nThe result is:", result)


def format_result(result):
    if DECIMAL_PRECISION is not None:
        if result == int(result):
            return int(result)
        else:
            return round(result, DECIMAL_PRECISION)
    else:
        return result


calculate()
