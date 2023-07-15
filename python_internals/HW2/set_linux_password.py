#!/usr/bin/env python3
import platform
import getpass
import subprocess
from string import digits, punctuation, ascii_lowercase, ascii_uppercase
from random import choice, shuffle


# import pwd


class LinuxPasswordManager:
    MIN_PASSWORD_LENGTH = 8
    DICTIONARY_WORDS = ["password", "123456", "qwerty", "abc123"]

    def __init__(self):
        self.username = None
        self.password = None

    def check_os_compatibility(self):
        """
        Checks whether the operating system is Linux.

        Causes:
            NonLinuxOperatingSystemError: If the operating system is not Linux.
        """
        try:
            os_name = platform.system()
            if os_name != "Linux":
                raise Exception(
                    f"This script is for Linux only. Please run it on a Linux machine. Your operating system: {os_name}"
                )
        except Exception as error:
            print(str(error))
            exit(1)

    def get_username(self):
        """
        Gets the username from the user input.
        """
        self.username = input("Enter a user name: ")

    def check_user_existence(self):
        """
        Checks if the entered username exists in the system.

        Returns:
            bool: True if the user exists, False otherwise.
        """
        try:
            subprocess.check_output(['id', self.username])
            return True
        except subprocess.CalledProcessError:
            return False

    def generate_password(self):
        """
        Generate a random password based on user input.

        Returns:
            str: The generated password

        Raises:
            ValueError: If the password length is less than 8
            Exception: If an unexpected error occurs while generating the password
        """
        print("Welcome to the Linux User Password Generator!\n")
        try:
            password_length = int(input("Please enter the desired password length (min: 8 | max: 32): "))
            if password_length < self.MIN_PASSWORD_LENGTH:
                raise ValueError(
                    f"The password length cannot be less than {self.MIN_PASSWORD_LENGTH}. Please try again.")

            password = [choice(ascii_lowercase), choice(ascii_uppercase), choice(digits), choice(punctuation)]

            length_over_4 = password_length - 4

            for _ in range(length_over_4):
                password.append(choice(ascii_lowercase + ascii_uppercase + digits + punctuation))
            shuffle(password)  # Shuffle the password characters

            password = ''.join(password)

            print(f"\nGenerated password: {password}")
            return password

        except ValueError as error:
            raise ValueError(str(error))
        except Exception as error:
            raise Exception(f"An unexpected error occurred while generating the password: {error}")

    def get_password(self):
        """
        Gets the password from the user input or generates a random password if no input is provided.
        """
        while not self.password:
            user_input = getpass.getpass("Enter a password or press Enter to generate one: ")
            if user_input:
                self.password = user_input
            else:
                self.password = self.generate_password()

    def check_password_requirements(self):
        """
        Checks if the password meets the requirements.

        Returns:
            bool: True if the password meets the requirements, False otherwise.
        """
        if len(self.password) < self.MIN_PASSWORD_LENGTH:
            return False

        if any(word in self.password for word in self.DICTIONARY_WORDS):
            return False

        return True

    def set_password(self):
        """
        Sets the user's password using the 'chpasswd' command with sudo privileges.
        """
        command = ['sudo', 'chpasswd']
        input_string = f"{self.username}:{self.password}"

        # Run the command with input string
        subprocess.run(command, input=input_string, text=True)

        # Save the password to a file
        with open("password.txt", "w") as file:
            file.write(f"Username: {self.username}\n")
            file.write(f"Password: {self.password}")

        print("The password was successfully set and saved in the password.txt file")

    def print_results(self):
        """
        Prints the username, password, and whether the password meets the requirements.
        """
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")
        print("The password meets the requirements." if self.check_password_requirements() else
              "The password does not meet the requirements.")

    def run(self):
        """
        Runs the password manager script.
        """
        self.check_os_compatibility()
        self.get_username()
        if not self.check_user_existence():
            print("The user does not exist. Please enter another user name.")
            return
        self.get_password()
        self.set_password()
        self.print_results()


# Create an instance of the class and run the script
password_manager = LinuxPasswordManager()
password_manager.run()
