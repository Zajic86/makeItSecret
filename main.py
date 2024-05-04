from file_operations import generate_key, encrypt_file, decrypt_file, list_files, list_key_files, InvalidKeyError


# main menu
def main_menu():
    print("________________________")
    print(" MAKE YOUR FILES SECURE")
    print("------------------------")
    while True:
        choice = input("Your choice:\n1. Generate key\n2. Encrypt file\n3. Decrypt file\n4. Exit\n")

        if choice == "1":
            key_name = input("Name of your secret .key file:")
            generate_key(key_name)
        elif choice == "2":
            list_files()
            filename = input("File for encrypting: ")
            list_key_files()
            key_filename = input("Name of your secret .key for encrypting: ")
            try:
                encrypt_file(filename, key_filename)
                print(f"File {filename} was encrypted")
            except FileNotFoundError:
                print("File not found, try again")
            except InvalidKeyError:
                print("Wrong .key file")
        elif choice == "3":
            list_files(".encrypted")
            filename = input("File for decrypting: ")
            list_key_files(".key")
            key_filename = input("Name of your secret .key for decrypting: ")
            try:
                decrypt_file(filename, key_filename)
                print(f"File {filename} was decrypted")
            except FileNotFoundError:
                print("File not found, try again")
            except InvalidKeyError:
                print("Wrong .key file")
        elif choice == "4":
            print("Exit")
            break
        else:
            print("Bad choice, try again")


if __name__ == "__main__":
    main_menu()
