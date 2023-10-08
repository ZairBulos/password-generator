from pathlib import Path
from cryptography.fernet import Fernet

KEY_FILE = Path('key.key')

def get_key():
    if not KEY_FILE.is_file():
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as file:
            file.write(key)
    return open(KEY_FILE, 'rb').read()

class CryptographyManager:
    def __init__(self):
        self.key = get_key()
        self.fernet = Fernet(self.key)

    def encrypt(self, data):
        try:
            encrypted = self.fernet.encrypt(data.encode('utf-8'))
            return encrypted
        except Exception as e:
            raise Exception(f'Error trying to encrypt: {str(e)}')

    def decrypt(self, data):
        try:
            decrypted = self.fernet.decrypt(data)
            return decrypted.decode('utf-8')
        except Exception as e:
            raise Exception(f'Error trying to decrypt: {str(e)}')