from password import generate_password
from cryptography_manager import CryptographyManager

data = generate_password()
print(f'Data: {data}')

cm = CryptographyManager()

encrypted_data = cm.encrypt(data)
print(f'Data encrypted: {encrypted_data}')

decrypted_data = cm.decrypt(encrypted_data)
print(f'Data decrypted: {decrypted_data}')