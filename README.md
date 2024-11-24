# EaseCrypt  

**EaseCrypt** is a Python-based file encryption and decryption tool designed to securely protect sensitive data. It uses AES-256 encryption through the `cryptography` library, ensuring robust data confidentiality and integrity.

---

## Features  
- **Key Generation:** Generates a secure 256-bit cryptographic key.  
- **File Encryption:** Converts files into an unreadable format, saving them with a `.encrypted` extension.  
- **File Decryption:** Restores original files from encrypted ones using the same cryptographic key.

---

## Prerequisites  
- Python 3.7 or higher installed on your system.  
- Required Python library: `cryptography`.  

Install the library using:  
```bash
pip install cryptography
```

---

## How to Use  

### 1. Key Generation  
Generate a cryptographic key by running the `generate_key.py` script.  
```bash
python generate_key.py
```  
- A file named `secret.key` will be created. This key is essential for both encryption and decryption.  
**Important:** Keep the key file secure and do not share it with unauthorized users.

---

### 2. File Encryption  
Encrypt a file using the `encrypt_file.py` script.  
```bash
python encrypt_file.py <file_path>
```  
- Replace `<file_path>` with the path of the file you want to encrypt.  
- The encrypted file will be saved in the same directory with a `.encrypted` extension.  

Example:  
```bash
python encrypt_file.py example.txt
```  
Output: `example.txt.encrypted`  

---

### 3. File Decryption  
Decrypt an encrypted file using the `decrypt_file.py` script.  
```bash
python decrypt_file.py <encrypted_file_path>
```  
- Replace `<encrypted_file_path>` with the path of the `.encrypted` file.  
- The decrypted file will be saved in the same directory, restoring the original file format and name.  

Example:  
```bash
python decrypt_file.py example.txt.encrypted
```  
Output: `example.txt`  

---

## Error Handling  
- **Missing Files:** If the specified file does not exist, an error message will be displayed.  
- **Incorrect Key:** Decryption will fail if the wrong key is used, ensuring security.  

---

## Notes  
- Ensure the `secret.key` file is kept secure and accessible during encryption and decryption.  
- Avoid hardcoding the key or sharing it publicly.  

---

## Future Enhancements  
- Adding password-based encryption.  
- Integrating a graphical user interface (GUI).  
- Secure key-sharing mechanisms for collaborative use.  

---

## License  
This project is licensed under the MIT License.  

---

## Acknowledgments  
Built with the `cryptography` library to ensure secure file encryption and decryption.