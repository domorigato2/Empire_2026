print("=========================================")
print("       CCNA MAC ADDRESS FORMATTER        ")
print("=========================================")

raw_mac = input("Enter MAC Address (any format): ").strip()

# Strip all common delimiters and convert to lowercase
clean_mac = raw_mac.replace(":", "").replace("-", "").replace(".", "").lower()

if len(clean_mac) != 12:
    print("\n[!] Invalid MAC Address. Must be exactly 12 hex characters.")
else:
    # Format 1: Linux / Standard (xx:xx:xx:xx:xx:xx)
    linux_mac = ":".join(clean_mac[i:i+2] for i in range(0, 12, 2))
    
    # Format 2: Windows (XX-XX-XX-XX-XX-XX)
    win_mac = "-".join(clean_mac[i:i+2] for i in range(0, 12, 2)).upper()
    
    # Format 3: Cisco (xxxx.xxxx.xxxx)
    cisco_mac = ".".join(clean_mac[i:i+4] for i in range(0, 12, 4))

    print("\n-----------------------------------------")
    print(f"RAW INPUT    : {raw_mac}")
    print(f"LINUX FORMAT : {linux_mac}")
    print(f"WINDOWS      : {win_mac}")
    print(f"CISCO IOS    : {cisco_mac}")
    print("-----------------------------------------")
    print("[✓] LAYER 2 HARDWARE ADDRESS FORMATTED.")

print("=========================================")