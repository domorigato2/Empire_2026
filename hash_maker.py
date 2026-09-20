import hashlib

print("=========================================")
print("      CCNA SECURITY: HASH GENERATOR      ")
print("=========================================")

password = input("Enter a password to encrypt (e.g., cisco123): ").strip()

if not password:
    print("[!] No password entered. Exiting.")
else:
    # Encode string to bytes
    encoded_pw = password.encode()
    
    # Generate Hashes
    md5_hash = hashlib.md5(encoded_pw).hexdigest()
    sha1_hash = hashlib.sha1(encoded_pw).hexdigest()
    sha256_hash = hashlib.sha256(encoded_pw).hexdigest()
    
    print("\n-----------------------------------------")
    print(f"PLAINTEXT : {password}")
    print("-----------------------------------------")
    print(f"MD5 (Type 5)   : {md5_hash}")
    print(f"SHA-1          : {sha1_hash}")
    print(f"SHA-256 (Type 8): {sha256_hash}")
    print("-----------------------------------------")
    print("[*] CCNA NOTE: MD5 is deprecated. Always use SHA-256 (enable algorithm-type scrypt secret).")
    print("=========================================")