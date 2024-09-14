import os
from cryptography.fernet import Fernet

# Load Key
def load_key():
    """Loads the secret key from a file."""
    return open('secret.key', 'rb').read()

# Encrypt File
def encrypt_file(file_name, output_folder):
    """Encrypts a file and saves it in the output folder."""
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, 'rb') as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)
    encrypted_file_name = os.path.join(output_folder, os.path.basename(file_name) + '.encrypted')

    with open(encrypted_file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File '{file_name}' encrypted successfully as '{encrypted_file_name}' with easeCrypt.")

# Encrypt Folder
def encrypt_folder(folder_path):
    """Encrypts all files in a folder and saves them in a new folder with '_encrypted' suffix."""
    output_folder = folder_path + '_encrypted'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, output_folder)

    print(f"All files in '{folder_path}' encrypted and saved to '{output_folder}'.")

# Menu Function
def menu():
    print("Welcome to easeCrypt - Encryption Tool")
    print("1. Encrypt a Single File")
    print("2. Encrypt a Folder")
    print("3. Encrypt an Image")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == '1':
        file_name = input("Enter the file name to encrypt: ")
        encrypt_file(file_name, os.path.dirname(file_name))
    elif choice == '2':
        folder_path = input("Enter the folder path to encrypt: ")
        encrypt_folder(folder_path)
    elif choice == '3':
        image_path = input("Enter the image file to encrypt: ")
        encrypt_image(image_path)
    elif choice == '4':
        print("Exiting easeCrypt...")
        return False  # Exit the loop
    else:
        print("Invalid option. Please try again.")
    return True  # Keep the loop running

if __name__ == "__main__":
    while menu():
        pass

