import sys
from cryptography.fernet import Fernet

def decrypt_file(filename):
    try:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
        f = Fernet(key)
        
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        
        decrypted_data = f.decrypt(encrypted_data)
        
        output_filename = filename.replace(".enc", ".decrypted")
        with open(output_filename, "wb") as file:
            file.write(decrypted_data)
            
        print(f"\n[+] '{filename}' decrypted to '{output_filename}'")
        with open(output_filename, "r") as f:
            print(f" [+] Content: {f.read().strip()}")
    except Exception as e:
        print(f"[!] Decryption Failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        decrypt_file(sys.argv[1])
    else:
        print("[!] Usage: python vault_decrypt.py <ENCRYPTED_FILE>")
