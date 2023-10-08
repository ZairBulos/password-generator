# Password Generator

The Password Generator is a Python program designed to generate random passwords, encrypt them using the [cryptography library](https://cryptography.io/en/latest/fernet/),
and store them in a file. This utility allows you to create and securely store passwords that can later be decrypted when needed.

## Requeriments

- [Python](https://www.python.org)

## Getting Started

1. Clone the repository

```bash
git clone https://github.com/ZairBulos/password-generator.git
```

2. Navigate to the project directory

3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the virtual environment

   - On Windows

    ```bash
    .\venv\Scripts\activate
    ```

    - On macOS/Linux

    ```bash
    source venv/bin/activate
    ```

5. Install the dependencies

```bash
pip install cryptography
```

6. Create a `.env` file in the root of the directory 

```env
LENGTH=26
FILE_NAME='YOUR_FILE_NAME'
```

## License

This project is Licensed under the [ISC](./LICENSE) License.