from cryptography.fernet import Fernet
import os


class InvalidKeyError(Exception):
    pass


# generate keys
def generate_key(key_name):
    key = Fernet.generate_key()
    key_filename = key_name + ".key"
    with open(key_filename, "wb") as key_file:
        key_file.write(key)
        print(f"OK - Your secret key has been generated and stored in the file {key_filename}")
        print("")


# encrypting file
def encrypt_file(filename, key_filename):
    try:
        with open(key_filename, "rb") as key_file:
            key = key_file.read()
            fernet = Fernet(key)
    except FileNotFoundError:
        raise FileNotFoundError
    try:
        with open(filename, "rb") as file:
            file_data = file.read()
            encrypted_data = fernet.encrypt(file_data)
        with open(filename + ".encrypted", "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
    except Exception:
        raise InvalidKeyError


# decrypting file
def decrypt_file(filename, key_filename):
    try:
        with open(key_filename, "rb") as key_file:
            key = key_file.read()
            fernet = Fernet(key)
    except FileNotFoundError:
        raise FileNotFoundError
    try:
        with open(filename, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()
            decrypted_data = fernet.decrypt(encrypted_data)
        with open(filename[:-10], "wb") as decrypted_file:  # remove apx ".encrypted"
            decrypted_file.write(decrypted_data)
    except Exception:
        raise InvalidKeyError


# list files
def list_files(extension=""):
    files = os.listdir()
    print("Files in directory")
    print("---------------------------------")
    for file in files:
        if file.endswith(extension):
            print(file)
    print("---------------------------------")


# list .key files
def list_key_files(extension=".key"):
    files = os.listdir()
    key_files = [file for file in files if file.endswith(extension)]
    print("Secret .key files in directory:")
    print("---------------------------------")
    for file in key_files:
        print(file)
    print("---------------------------------")
