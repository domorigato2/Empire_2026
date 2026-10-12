import sys
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("\n[+] Cryptographic Master Key generated: 'secret.key'")

def encrypt_file(filename):
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted_data = f.encrypt(data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)
    print(f"[+] '{filename}' encrypted to '{filename}.enc'")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[!] Usage: python vault_engine.py <init | encrypt <file>>")
    elif sys.argv[1] == "init":
        generate_key()
    elif sys.argv[1] == "encrypt":
        encrypt_file(sys.argv[2])
