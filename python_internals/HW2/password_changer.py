# #!/usr/bin/env python3
#
#
# import subprocess
# import random
#
#
# class PasswordChanger:
#     def __init__(self):
#         # Initialize variables and check user context/env variables
#         pass
#
#     def check_user_existence(self, username):
#         # Check if user exists in the system
#         pass
#
#     def get_password_requirements(self):
#         # Interact with the user to gather password complexity criteria
#         pass
#
#     def generate_password(self):
#         # Generate a random password based on the specified requirements
#         pass
#
#     def set_password(self, username, password):
#         # Set the password for the user
#         pass
#
#     def run(self):
#         # Coordinate the execution of the script
#         pass
#
#
# if __name__ == '__main__':
#     password_changer = PasswordChanger()
#     password_changer.run()

# !/usr/bin/env python3
import subprocess
import getpass
import os
import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import shutil


class PasswordChanger:
    def __init__(self, username):
        self.username = username

    def check_user_exists(self):
        """
        Check if the user exists in the system.
        """
        try:
            subprocess.check_output(['id', self.username])
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to check user existence: {e}")
            return False
        except Exception as e:
            print(f"Error: An unexpected error occurred while checking user existence: {e}")
            return False

    def generate_password(self):
        """
        Generate a random password based on user input.
        """
        print("Welcome to the Linux User Password Generator!\n")
        try:
            password_length = int(input("Please enter the desired password length: "))
            if password_length < 4:
                raise ValueError("Error: The password length cannot be less than 4. Please try again.")
            password = [random.choice(ascii_lowercase), random.choice(ascii_uppercase), random.choice(digits),
                        random.choice(punctuation)]

            length_over_4 = password_length - 4

            for _ in range(length_over_4):
                password.append(random.choice(ascii_lowercase + ascii_uppercase + digits + punctuation))

            password = ''.join(password)

            print(f"\nGenerated password: {password}")
            return password

        except ValueError as e:
            print(e)
            return None
        except Exception as e:
            print(f"Error: An unexpected error occurred while generating the password: {e}")
            return None

    def check_password_requirements(self, password):
        """
        Check if the password meets the requirements.
        """
        try:
            if len(password) >= 8 and any(char.isupper() for char in password) and \
                    any(char.islower() for char in password) and any(char.isdigit() for char in password):
                return True
            else:
                return False
        except Exception as e:
            print(f"Error: An unexpected error occurred while checking password requirements: {e}")
            return False

    def change_password(self, password):
        """
        Change the user's password using chpasswd command.
        """
        try:
            if os.geteuid() != 0:
                print("Error: This operation requires root privileges.")
                return

            if subprocess.call(['echo', f"{self.username}:{password}"] | ['chpasswd']) != 0:
                print("Error: Failed to change the password.")
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to change the password: {e}")
        except Exception as e:
            print(f"Error: An unexpected error occurred while changing the password: {e}")

    def get_current_user(self):
        """
        Get the current user context.
        """
        try:
            return os.getenv("USER")
        except Exception as e:
            print(f"Error: An unexpected error occurred while getting the current user: {e}")
            return None

    def check_required_utilities(self):
        """
        Check if the required system utilities are available.
        """
        required_utilities = ['id', 'chpasswd']
        missing_utilities = []

        for utility in required_utilities:
            if not shutil.which(utility):
                missing_utilities.append(utility)

        if missing_utilities:
            print(f"Error: The following required system utilities are missing: {', '.join(missing_utilities)}")
            return False
        else:
            return True

    def run(self):
        """
        Run the password change process.
        """
        try:
            if not self.check_user_exists():
                print("User does not exist.")
                return

            password = getpass.getpass("Enter a new password (leave blank to generate one): ")
            if not password:
                password = self.generate_password()

            if not self.check_password_requirements(password):
                print("Password does not meet the requirements.")
                return

            self.change_password(password)
            print(f"Password changed for user {self.username}.")
            print(f"New password: {password}")
            print("Password meets the requirements.")

            current_user = self.get_current_user()
            if current_user:
                print(f"Current user context: {current_user}")
            else:
                print("Error: Failed to get the current user context.")
        except Exception as e:
            print(f"Error: An unexpected error occurred while running the program: {e}")


def main():
    username = input("Enter the username: ")
    password_changer = PasswordChanger(username)

    if not password_changer.check_required_utilities():
        return

    password_changer.run()


if __name__ == "__main__":
    main()
