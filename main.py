import string
def encrypt(text, key):
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    numbers = string.digits
    result = ""

    for c in text:
        if c.isalpha():
            alphabet = alphabet_lower if c.islower() else alphabet_upper
            new_index = (alphabet.index(c) + key) % 26
            result += alphabet[new_index]
        elif c.isdigit():
            new_index = (numbers.index(c) + key) % 10
            result += numbers[new_index]
        else:
            result += c  # Keep punctuation & spaces unchanged

    return result


def decrypt(text, key):
    return encrypt(text, -key)  # Reuse the encryption function with a negative key


def find_key(crypt_text, uncrypt_text):
    if len(crypt_text) != len(uncrypt_text):
        print("NOT VALID: Lengths of the words don't match!")
        return -1

    for c, u in zip(crypt_text, uncrypt_text):
        if c.isalpha() and u.isalpha():
            alphabet = string.ascii_lowercase if c.islower() else string.ascii_uppercase
            key = (alphabet.index(c) - alphabet.index(u)) % 26
            return key
        elif c.isdigit() and u.isdigit():
            key = (string.digits.index(c) - string.digits.index(u)) % 10
            return key
        elif c != u:
            print("NOT VALID: Mismatch between letters and numbers!")
            return -1

    return 0


def decrypt_without_key(text):
    for key in range(1, 26):
        print(f"Trying key {key}: {decrypt(text, key)}")


def main():
    while True:
        print("""

        ░█████╗░███████╗░█████╗░░██████╗░█████╗░██████╗░░░░░░██╗░█████╗░░██╗░░░░░░░██╗
        ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗░░░░░██║██╔══██╗░██║░░██╗░░██║
        ██║░░╚═╝█████╗░░███████║╚█████╗░███████║██████╔╝░░░░░██║███████║░╚██╗████╗██╔╝
        ██║░░██╗██╔══╝░░██╔══██║░╚═══██╗██╔══██║██╔══██╗██╗░░██║██╔══██║░░████╔═████║░
        ╚█████╔╝███████╗██║░░██║██████╔╝██║░░██║██║░░██║╚█████╔╝██║░░██║░░╚██╔╝░╚██╔╝░
        ░╚════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░

                                    by Mohammed Mehdi Boudir & Salah Eddine Rhazouni
            """)
        print("Do you want to Encrypt(1), Decrypt(2), Find Key(3), or Decrypt without key(4) ?")
        print("[*] Enter Option (1,2,3 or 4) : ")
        choice = input().strip()

        if choice not in {"1", "2", "3", "4"}:
            print("ERROR: Invalid choice ! Please enter 1, 2, 3, or 4 !")
            continue

        if choice in {"1", "2"}:
            while True:
                try:
                    key = int(input("[*] Enter Shift Key (an integer): "))
                    if key < 0:
                        print("ERROR: Invalid Switch Key! Please enter a positive key !")
                        continue
                    break
                except ValueError:
                    print("ERROR: Please enter a valid integer key !")

            text = input("[*] Please enter text: \n")
            print("==> Output Result :")
            print(encrypt(text, key) if choice == "1" else decrypt(text, key))

        elif choice == "3":
            crypt_text = input("[*] Please enter encrypted text: \n")
            uncrypt_text = input("[*] Please enter decrypted text: \n")
            key = find_key(crypt_text, uncrypt_text)
            if key != -1:
                print("Shift Key:", key)

        elif choice == "4":
            text = input("[*] Please enter text to decrypt without a key: \n")
            decrypt_without_key(text)

        repeat = input("Do you want to try again? (Y/N): ").strip().lower()
        if repeat not in {"y", "yes"}:
            print("Thank you for using the program.")
            break

if __name__ == "__main__":
    main()
