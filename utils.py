def get_user_input() -> tuple:
    while True:
        try:
            length = int(input("Enter the password length: "))
            quantity = int(input("Enter the number of passwords: "))
            if length <= 0 or quantity <= 0:
                raise ValueError("Values must be positive!")
            return length, quantity
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.\n")


def display_passwords(passwords: list):
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"{i}: {password}")
