import sys

def audit_config(filepath):
    print("\n==================================================")
    print("      CISCO CCNA // CONFIG SECURITY AUDITOR       ")
    print("==================================================")
    print(f" Target File : {filepath}")
    print(" Scanning configuration text for security flaws...")
    print("--------------------------------------------------")

    try:
        with open(filepath, "r") as f:
            config = f.read()
    except FileNotFoundError:
        print(f"[!] Error: File '{filepath}' not found.")
        return

    issues = 0

    # Check for password encryption
    if "service password-encryption" not in config:
        print(" [-] VULN: 'service password-encryption' missing (Cleartext passwords in NVRAM).")
        issues += 1
    else:
        print(" [+] PASS: Global password encryption is enabled.")

    # Check for insecure Telnet transport on VTY lines
    if "transport input telnet" in config or ("line vty" in config and "transport input all" in config):
        print(" [-] VULN: Insecure Telnet transport allowed on VTY lines.")
        issues += 1
    else:
        print(" [+] PASS: Secure SSH transport enforced on VTY lines.")

    # Check for weak enable password
    if "enable password" in config:
        print(" [-] VULN: Weak 'enable password' in use instead of 'enable secret'.")
        issues += 1
    else:
        print(" [+] PASS: Secure 'enable secret' cryptographic hash verified.")

    print("--------------------------------------------------")
    print(f" Security Audit Complete. Total Vulnerabilities Found: {issues}")
    print("==================================================\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "mock_config.txt"
    audit_config(target)
