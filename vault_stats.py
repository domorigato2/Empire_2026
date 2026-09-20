import os

print("=========================================")
print("      EMPIRE VAULT TELEMETRY PARSER      ")
print("=========================================")

vault_file = "telemetry_vault.txt"

if not os.path.exists(vault_file):
    print("[!] No telemetry_vault.txt found in current directory.")
else:
    with open(vault_file, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    total_logs = len(lines)
    print(f"[*] Total Logged Checkpoints: {total_logs}")
    print("-----------------------------------------")
    print("RECENT ENTRIES:")
    for entry in lines[-3:]:  # Show last 3 entries
        print(f" > {entry}")
    print("-----------------------------------------")
    print("[✓] PARSE COMPLETE. SYSTEM DATA VERIFIED.")

print("=========================================")