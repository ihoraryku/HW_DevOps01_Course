#!/usr/bin/env python3

from password_changer import UserPasswordChanger

def main():
    try:
        # Check the operating system
        import platform
        if platform.system() != "Linux":
            raise Exception("This operating system is not Linux. The script is designed to work only with Linux.")

        # Prompt the user to enter the username
        username = input("Enter the username: ")

        # Create an instance of UserPasswordChanger with the provided username
        password_changer = UserPasswordChanger(username)

        # Run the password change process
        password_changer.run()
    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()

