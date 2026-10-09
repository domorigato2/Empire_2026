import string
import random
import sys

def generate_password(length=16):
    print("\n==================================================")
    print("      TACTICAL CRYPTO // SECURE PASSWORD GEN      ")
    print("==================================================")
    
    # Pool of ASCII letters, digits, and punctuation symbols
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # Generate high-entropy string
    password = "".join(random.choice(alphabet) for _ in range(length))
    
    print(f" Key Length : {length} Characters")
    print(f" Secure Key : {password}")
    print("==================================================\n")

if __name__ == "__main__":
    length = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    generate_password(length)
