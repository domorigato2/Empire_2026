import base64
import sys

def b64_process(mode, text):
    print("\n==================================================")
    print("      TACTICAL CRYPTO // BASE64 ENGINE            ")
    print("==================================================")
    try:
        if mode == "encode":
            encoded_bytes = base64.b64encode(text.encode('utf-8'))
            result = encoded_bytes.decode('utf-8')
            print(f" [ENCODE] Plaintext : {text}")
            print(f" [RESULT] Base64    : {result}")
        elif mode == "decode":
            decoded_bytes = base64.b64decode(text.encode('utf-8'))
            result = decoded_bytes.decode('utf-8')
            print(f" [DECODE] Base64    : {text}")
            print(f" [RESULT] Plaintext : {result}")
        else:
            print("[!] Invalid mode. Use 'encode' or 'decode'.")
    except Exception as e:
        print(f"[!] Processing Error: {e}")
    print("==================================================\n")

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        m = sys.argv[1].lower()
        t = " ".join(sys.argv[2:])
        b64_process(m, t)
    else:
        print("[!] Usage: python b64_engine.py <encode/decode> <text>")
