from cryptography_manager import CryptographyManager
from utils import input_option, encrypt_password, decrypt_password, read_file

def main():
    cm = CryptographyManager()
    switch(cm)

def menu():
    print('1. Generate a random password and encrypt')
    print('2. Decrypt a password')
    print('3. Read file')
    print('4. Exit')

def switch(cm):
    while True:
        menu()
        option = input_option(min=1, max=4)

        if option == 1:
            encrypt_password(cm)
        elif option == 2:
            decrypt_password(cm)
        elif option == 3:
            read_file()
        elif option == 4:
            break

if __name__ == '__main__':
    main()