import random
from string import printable

print("Welcome to the Linux User Password Generator!\n")


def pas_generate():
    password_length = int(input("Please enter the desired password length: "))
    password = ""

    for _ in range(password_length):
        password += random.choice(list(printable))

    print(f"\nGenerated password: {password}")


pas_generate()
