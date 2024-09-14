import os
from cryptography.fernet import Fernet

# Load Key
def load_key():
    """Loads the secret key from a file."""
    return open('secret.key', 'rb').read()

# Decrypt File
def decrypt_file(file_name, output_folder):
    """Decrypts a file and saves it in the output folder."""
    key = load_key()
    fernet = Fernet(key)

    try:
        with open(file_name, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        decrypted_data = fernet.decrypt(encrypted_data)
        original_file_name = os.path.join(output_folder, os.path.basename(file_name).replace('.txt.encrypted', '.decrypted.txt'))
        original_file_name = os.path.join(output_folder, os.path.basename(file_name).replace('.encrypted', ''))

        with open(original_file_name, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
        print(f"File '{file_name}' decrypted successfully as '{original_file_name}' with easeCrypt.")
    except Exception as e:
        print(f"Error: {e}. Incorrect key or corrupted file.")

# Decrypt Folder
def decrypt_folder(folder_path):
    """Decrypts all files in a folder and saves them in a new folder with '_decrypted' suffix."""
    output_folder = folder_path.replace('_encrypted', '_decrypted')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.encrypted'):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, output_folder)

    print(f"All files in '{folder_path}' decrypted and saved to '{output_folder}'.")

# Menu Function
def menu():
    print("Welcome to easeCrypt - Decryption Tool")
    print("1. Decrypt a Single File")
    print("2. Decrypt a Folder")
    print("3. Decrypt an Image")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == '1':
        file_name = input("Enter the encrypted file name to decrypt: ")
        decrypt_file(file_name, os.path.dirname(file_name))
    elif choice == '2':
        folder_path = input("Enter the folder path to decrypt: ")
        decrypt_folder(folder_path)
    elif choice == '3':
        image_path = input("Enter the encrypted image file to decrypt: ")
        decrypt_image(image_path)
    elif choice == '4':
        print("Exiting easeCrypt...")
        return False  # Exit the loop
    else:
        print("Invalid option. Please try again.")
    return True  # Keep the loop running

if __name__ == "__main__":
    while menu():
        pass

