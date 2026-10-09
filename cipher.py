import sys

def caesar(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift
        
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # Circular 26-letter shift
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char
    return result

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        mode = sys.argv[1].lower()  # "encrypt" or "decrypt"
        shift_val = int(sys.argv[2])
        raw_text = " ".join(sys.argv[3:])
        
        output = caesar(raw_text, shift_val, mode)
        
        print("\n========================================")
        print(f"      CYBERNETIC CIPHER ENGINE [{mode.upper()}]")
        print("========================================")
        print(f" Input  : {raw_text}")
        print(f" Shift  : {shift_val}")
        print(f" Output : {output}")
        print("========================================\n")
    else:
        print("[!] Usage: python cipher.py <encrypt/decrypt> <shift_key> <text>")
