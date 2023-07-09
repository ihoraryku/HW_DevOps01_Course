#!/usr/bin/env python3


from random import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import pyperclip

MAX_PASSWORD_LENGTH = 32
MAX_ATTEMPTS = 3


def welcome_message():
    print("Welcome to the Linux User Password Generator!\n")


def get_password_length():
    for _ in range(MAX_ATTEMPTS):
        try:
            password_length = input("\nPlease enter the desired password length: ")

            if not password_length.isdigit():
                raise ValueError(
                    f"\nThe entered password length is invalid! \nPlease enter an integer number between 4 and {MAX_PASSWORD_LENGTH}.")

            password_length = int(password_length)

            if password_length < 4 or password_length > MAX_PASSWORD_LENGTH:
                raise ValueError(
                    f"\nThe entered password length is invalid! \nPlease enter the length again, it should be between 4 and {MAX_PASSWORD_LENGTH} characters.")

            return password_length

        except ValueError as error:
            print(error)

    print("\nThe maximum number of incorrect data entry attempts has been reached. Exiting...")
    return None


def generate_password(password_length):
    password = [choice(ascii_lowercase), choice(ascii_uppercase), choice(digits), choice(punctuation)]

    length_over_4 = password_length - 4

    for _ in range(length_over_4):
        password.append(choice(ascii_lowercase + ascii_uppercase + digits + punctuation))

    password = ''.join(password)
    return password


def copy_password_to_clipboard(password):
    save_to_clipboard = input("\nCopy password to clipboard? (yes or no(default)): ").lower()

    if save_to_clipboard == 'yes':
        pyperclip.copy(password)
        print("\nPassword copied to clipboard.")
    else:
        print("\nThe password is not copied to the clipboard.")


def save_password_to_file(password):
    save_to_file = input("\nSave password to file? (yes or no(default)): ").lower()

    if save_to_file == 'yes':
        with open("password.txt", "w") as file:
            file.write(password)
        print("\nPassword saved to file.")
    else:
        print("\nThe password is not saved to the file.")


def pas_generate():
    welcome_message()
    password_length = get_password_length()

    if password_length is not None:
        password = generate_password(password_length)
        print(f"\nGenerated password: {password}")

        copy_password_to_clipboard(password)
        save_password_to_file(password)


pas_generate()
