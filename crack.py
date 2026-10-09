import sys

def crack_caesar(ciphertext):
    print("\n==================================================")
    print(f"   BRUTE-FORCE CIPHER BREAKER // 25 KEY MATRIX   ")
    print("==================================================")
    print(f" TARGET CIPHERTEXT: {ciphertext}\n")
    
    for shift in range(1, 26):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - start - shift) % 26 + start)
                decrypted += new_char
            else:
                decrypted += char
        print(f" [KEY {shift:02d}] --> {decrypted}")
        
    print("==================================================\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = " ".join(sys.argv[1:])
        crack_caesar(target)
    else:
        print("[!] Usage: python crack.py <ENCRYPTED_TEXT>")
