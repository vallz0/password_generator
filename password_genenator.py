import random
import string

class PasswordGenerator:
    def __init__(self, length: int, quantity: int):
        self.length = length
        self.quantity = quantity
        self.characters = string.ascii_letters + string.digits + "!@#$%&"

    def generate_password(self) -> str:
        return ''.join(random.choice(self.characters) for _ in range(self.length))

    def generate_passwords(self) -> list:
        return [self.generate_password() for _ in range(self.quantity)]
