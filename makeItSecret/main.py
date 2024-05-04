from file_operations import generate_keypair, encrypt_file, decrypt_file, list_files, list_key_files, InvalidKeyError


# main menu
def main_menu():
    print("________________________")
    print(" MAKE YOUR FILES SECURE")
    print("------------------------")
    while True:
        choice = input("Your choice:\n1. Generate key\n2. Encrypt file\n3. Decrypt file\n4. Exit\n")

        if choice == "1":
            generate_keypair()
        elif choice == "2":
            list_files()
            filename = input("File for encrypting: ")
            list_key_files()
            public_key_file = input("Name of PUBLIC key (.pem file): ")
            try:
                encrypt_file(filename, public_key_file)
                print(f"File {filename} was encrypted.")
            except FileNotFoundError:
                print("File not found, try again")
            except InvalidKeyError:
                print("Wrong .pem file")
        elif choice == "3":
            list_files(".encrypted")
            filename = input("Name of file for decrypting: ")
            list_key_files()
            private_key_file = input("Name of PRIVATE key (.pem file): ")
            try:
                decrypt_file(filename, private_key_file)
                print(f"File {filename} was decrypted")
            except InvalidKeyError:
                print("Wrong decrypting (PRIVATE) key")
        elif choice == "4":
            print("Exit")
            break
        else:
            print("Bad choice, try again")


if __name__ == "__main__":
    main_menu()
