#TASK 3 :- PASSWORD GENERATOR

"""A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password"""

import random
import string

def generate_password(length, complexity):
    if complexity == "1":
        characters = string.ascii_letters
    elif complexity == "2":
        characters = string.ascii_letters + string.digits
    elif complexity == "3":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("\nPassword Generator")

    while True:
        length = int(input("Enter the desired length of the password: "))
        print("\nChoose Complexity Level\n1. Low\n2. Medium\n3. High")
        complexity = input("Enter complexity level: ").lower()

        password = generate_password(length, complexity)

        if password:
            print("\nGenerated Password:", password)

        another_password = input("\nDo you want to generate another password? (Y/N): ")
        if another_password.lower() not in ["yes", "y","Y"]:
            break
          
if __name__ == "__main__":
    main()
