# generate_key.py
from cryptography.fernet import Fernet

def generate_key():
    """Generates a secret key and saves it to a file."""
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)
    print("Secret key generated and saved to 'secret.key'.")

if __name__ == "__main__":
    print("Welcome to easeCrypt - Key Generation")
    generate_key()

