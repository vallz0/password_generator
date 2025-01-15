from operator import length_hint

from password_genenator import PasswordGenerator
from utils import get_user_input, display_passwords

class PasswordApp:
    def run(self):
        print("Welcome to the Password Generator")
        length, quantity = get_user_input()
        generator = PasswordGenerator(length,quantity)
        passwords = generator.generate_passwords()
        display_passwords(passwords)

if __name__ == '__main__':
    app = PasswordApp()
    app.run()