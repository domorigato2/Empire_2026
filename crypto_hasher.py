import hashlib
import sys

def generate_hashes(text):
    print("\n==================================================")
    print("      TACTICAL CRYPTO // HASH GENERATOR           ")
    print("==================================================")
    print(f" Input String : {text}")
    print("--------------------------------------------------")
    
    # Compute MD5 and SHA-256
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    
    print(f" [MD5   ] {md5_hash}")
    print(f" [SHA256] {sha256_hash}")
    print("==================================================\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_text = " ".join(sys.argv[1:])
        generate_hashes(target_text)
    else:
        print("[!] Usage: python crypto_hasher.py <TEXT_TO_HASH>")
