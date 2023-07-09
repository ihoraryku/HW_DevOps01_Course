#!/usr/bin/env python3

from random import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

MAX_PASSWORD_LENGTH = 32
MAX_ATTEMPTS = 3


def pas_generate():
    print("Welcome to the Linux User Password Generator!\n")
    for _ in range(MAX_ATTEMPTS):
        try:
            password_length = int(input("\nPlease enter the desired password length: "))
            if password_length < 4 or password_length > MAX_PASSWORD_LENGTH:
                print(
                    "\nThe entered password length is invalid! \nPlease enter the length again, it should be between 4 and 32 characters.")
                continue

            password = [choice(ascii_lowercase), choice(ascii_uppercase), choice(digits),
                        choice(punctuation)]

            length_over_4 = password_length - 4

            for _ in range(length_over_4):
                password.append(choice(ascii_lowercase + ascii_uppercase + digits + punctuation))

            password = ''.join(password)

            print(f"\nGenerated password: {password}")

            save_to_file = input("\nSave password to file (yes or no)? ").lower()
            if save_to_file == 'yes':
                with open("password.txt", "w") as file:
                    file.write(password)
                    print("Password saved to file.")

            return

        except ValueError as error:
            print(error)

    print("\nThe maximum number of incorrect data entry attempts has been reached. Exit...")


pas_generate()

from random import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

MAX_PASSWORD_LENGTH = 32
MAX_ATTEMPTS = 3


def pas_generate():
    print("Welcome to the Linux User Password Generator!\n")

    for attempt in range(MAX_ATTEMPTS):
        try:
            password_length = input("\nPlease enter the desired password length: ")

            if not password_length.isdigit():
                raise ValueError("The entered password length is not a number!")

            password_length = int(password_length)

            if password_length < 4 or password_length > MAX_PASSWORD_LENGTH:
                raise ValueError(
                    "The entered password length is invalid! Please enter the length again, it should be between 4 and 32 characters.")

            password = [choice(ascii_lowercase), choice(ascii_uppercase), choice(digits), choice(punctuation)]

            length_over_4 = password_length - 4

            for _ in range(length_over_4):
                password.append(choice(ascii_lowercase + ascii_uppercase + digits + punctuation))

            password = ''.join(password)

            if password.startswith('_'):
                print("Generated password starts with '_', generating a new one...")
                continue

            print(f"\nGenerated password: {password}")

            save_to_file = input("\nSave password to file (yes or no)? ").lower()

            if save_to_file == 'yes':
                with open("password.txt", "w") as file:
                    file.write(password)
                print("Password saved to file.")

            return

        except ValueError as error:
            print(error)

    print("\nThe maximum number of incorrect data entry attempts has been reached. Exiting...")


pas_generate()
