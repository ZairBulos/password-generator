from config import FILE
from password import generate_password

def input_option(min, max):
    try:
        option = int(input('Enter a option: '))
        if min <= option <= max:
            return option
        else:
            raise ValueError
    except:
        print('Invalid input. Please enter a valid option.')

def write_file(data):
    try:
        with open(file=FILE, mode='ab') as file:
            file.write(data)
    except:
        raise Exception('Error trying to write the file')

def read_file():
    try:
        with open(file=FILE, mode='rb') as file:
            data = file.read()
        print(data.decode('utf-8'))
    except:
        raise Exception('Error trying to read the file')

def encrypt_password(cm):
    try:
        new_password = generate_password()
        encrypted_password = cm.encrypt(data=new_password)

        line = input('What is this password for?: ')
        data = f'{line} == {encrypted_password.decode("utf-8")}\n'
        data_encoded = data.encode('utf-8')
        write_file(data=data_encoded)

        print(f'Your password for {line} is {new_password}')
    except Exception as e:
        print(f'{str(e)}')

def decrypt_password(cm):
    try:
        data = input('Enter your encrypted password: ')
        decrypted_password = cm.decrypt(data)

        print(f'Your decrypted password is {decrypted_password}')
    except Exception as e:
        print(f'{str(e)}')