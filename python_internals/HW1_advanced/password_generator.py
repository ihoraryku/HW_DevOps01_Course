import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

print("Welcome to the Linux User Password Generator!\n")


def pas_generate():
    password_length = int(input("Please enter the desired password length: "))
    password = [random.choice(ascii_lowercase), random.choice(ascii_uppercase), random.choice(digits),
                random.choice(punctuation)]

    length_over_4 = password_length - 4

    for _ in range(length_over_4):
        password.append(random.choice(ascii_lowercase + ascii_uppercase + digits + punctuation))

    password = ''.join(password)

    print(f"\nGenerated password: {password}")


pas_generate()
