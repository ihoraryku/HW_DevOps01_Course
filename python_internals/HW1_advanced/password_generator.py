import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

print("Welcome to the Linux User Password Generator!\n")


def pas_generate():
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

    except ValueError as e:
        print(e)


pas_generate()
