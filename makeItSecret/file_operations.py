from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
import os


class InvalidKeyError(Exception):
    pass


# generate keys
def generate_keypair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    with open("private_key.pem", "wb") as private_key_file:
        private_key_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )
        print("private_key.pem file was created. This is secret key for you!")

    with open("public_key.pem", "wb") as public_key_file:
        public_key_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )
        print("public_key.pem was created. This is key for everyone, make it public")


# encrypting file
def encrypt_file(filename, public_key_file):
    try:
        with open(public_key_file, "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=None
            )
    except FileNotFoundError:
        raise FileNotFoundError
    try:
        with open(filename, "rb") as file:
            file_data = file.read()
            encrypted_data = public_key.encrypt(
                file_data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        with open(filename + ".encrypted", "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
    except Exception:
        raise InvalidKeyError


# decrypting file
def decrypt_file(filename, private_key_file):
    with open(private_key_file, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=None
        )
    with open(filename, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
        try:
            decrypted_data = private_key.decrypt(
                encrypted_data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            with open(filename[:-10], "wb") as decrypted_file:  # remove apx ".encrypted"
                decrypted_file.write(decrypted_data)
        except ValueError:
            raise InvalidKeyError("Wrong key for decrypting")


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
def list_key_files(extension=".pem"):
    files = os.listdir()
    key_files = [file for file in files if file.endswith(extension)]
    print("Secret .pem files in directory:")
    print("---------------------------------")
    for file in key_files:
        print(file)
    print("---------------------------------")
