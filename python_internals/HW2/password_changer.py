import subprocess
import getpass
import os
import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


class UserPasswordChanger:
    def __init__(self, username):
        self.username = username

    @staticmethod
    def generate_password():
        """
        Generate a random password based on user input.
        """
        print("Welcome to the Linux User Password Generator!\n")
        try:
            password_length = int(input("Please enter the desired password length: "))
            if password_length < 4:
                raise ValueError("The password length cannot be less than 4. Please try again.")
            password = [random.choice(ascii_lowercase), random.choice(ascii_uppercase), random.choice(digits),
                        random.choice(punctuation)]

            length_over_4 = password_length - 4

            for _ in range(length_over_4):
                password.append(random.choice(ascii_lowercase + ascii_uppercase + digits + punctuation))

            password = ''.join(password)

            print(f"\nGenerated password: {password}")
            return password

        except ValueError as error:
            raise Exception(str(error))
        except Exception as error:
            raise Exception(f"An unexpected error occurred while generating the password: {error}")

    @staticmethod
    def check_password_requirements(password):
        """
        Check if the password meets the requirements.
        """
        try:
            # Check the length and character types of the password
            if len(password) >= 8 and any(char.isupper() for char in password) and \
                    any(char.islower() for char in password) and any(char.isdigit() for char in password):
                return True
            else:
                return False
        except Exception as error:
            raise Exception(f"An unexpected error occurred while checking password requirements: {error}")

    @staticmethod
    def get_current_user():
        """
        Get the current user context.
        """
        try:
            # Get the current user from the environment variables
            return os.getenv("USER")
        except Exception as error:
            raise Exception(f"An unexpected error occurred while getting the current user: {error}")

    def check_user_exists(self):
        """
        Check if the user exists in the system.
        """
        try:
            # Use the 'id' command to check if the user exists
            subprocess.check_output(['id', self.username])
            return True
        except subprocess.CalledProcessError:
            raise Exception(f"User '{self.username}' does not exist.")
        except Exception as error:
            raise Exception(f"Failed to check user existence: {error}")

    def change_password(self, password):
        """
        Change the user's password using chpasswd command.
        """
        try:
            # Check if the program has root privileges
            if os.geteuid() != 0:
                raise Exception("This operation requires root privileges.")

            # Execute the chpasswd command to change the user's password
            echo_process = subprocess.Popen(['echo', f"{self.username}:{password}"], stdout=subprocess.PIPE)
            chpasswd_process = subprocess.Popen(['chpasswd'], stdin=echo_process.stdout)

            # Wait for the chpasswd process to complete
            chpasswd_process.wait()

            if chpasswd_process.returncode != 0:
                raise Exception("Failed to change the password.")
        except subprocess.CalledProcessError as error:
            raise Exception(f"Failed to change the password: {error}")
        except Exception as error:
            raise Exception(f"An unexpected error occurred while changing the password: {error}")

    def run(self):
        """
        Run the password change process.
        """
        try:
            # Check if the user exists
            if not self.check_user_exists():
                raise Exception(f"User '{self.username}' does not exist.")

            # Prompt the user to enter a new password or generate one
            password = getpass.getpass("Enter a new password (leave blank to generate one): ")
            if not password:
                password = UserPasswordChanger.generate_password()

            # Check if the password meets the requirements
            if not UserPasswordChanger.check_password_requirements(password):
                raise Exception("Password does not meet the requirements.")

            # Change the user's password
            self.change_password(password)
            print(f"Password changed for user '{self.username}'.")
            print(f"New password: {password}")
            print("Password meets the requirements.")

            # Get the current user context
            current_user = UserPasswordChanger.get_current_user()
            if current_user:
                print(f"Current user context: {current_user}")
            else:
                raise Exception("Failed to get the current user context.")
        except Exception as error:
            raise Exception(f"An error occurred while running the program: {error}")
