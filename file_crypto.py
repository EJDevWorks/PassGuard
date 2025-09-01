from cryptography.fernet import Fernet
import os
from typing import Optional

def get_fernet(key_file: str = os.path.join('data', 'filekey.key')) -> Fernet:
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
    else:
        with open(key_file, 'rb') as f:
            key = f.read()
    return Fernet(key)

def encrypt_file(input_path: str, output_path: Optional[str] = None, key_file: str = os.path.join('data', 'filekey.key')) -> str:
    """Encrypts a file and saves it as <input_path>.encrypted or output_path in data folder. Deletes original file after encryption."""
    fernet = get_fernet(key_file)
    with open(input_path, 'rb') as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    if not output_path:
        base = os.path.basename(input_path)
        output_path = os.path.join('data', base + '.encrypted')
    with open(output_path, 'wb') as f:
        f.write(encrypted)
    # Delete original file after encryption
    try:
        os.remove(input_path)
    except Exception:
        pass
    return output_path

def decrypt_file(input_path: str, output_path: Optional[str] = None, key_file: str = os.path.join('data', 'filekey.key')) -> str:
    """Decrypts a file and saves it as <input_path>.decrypted or output_path in data folder. Deletes encrypted file after decryption."""
    fernet = get_fernet(key_file)
    with open(input_path, 'rb') as f:
        encrypted = f.read()
    decrypted = fernet.decrypt(encrypted)
    if not output_path:
        base = os.path.basename(input_path)
        output_path = os.path.join('data', base + '.decrypted')
    with open(output_path, 'wb') as f:
        f.write(decrypted)
    # Delete encrypted file after decryption
    try:
        os.remove(input_path)
    except Exception:
        pass
    return output_path

if __name__ == '__main__':
    # Example usage
    # Encrypt a file
    encrypted_path = encrypt_file('yourfile.txt')
    print(f'Encrypted file saved as: {encrypted_path}')

    # Decrypt a file
    decrypted_path = decrypt_file(encrypted_path)
    print(f'Decrypted file saved as: {decrypted_path}')
