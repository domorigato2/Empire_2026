print("=========================================")
print("      CCNA IPv4 BINARY CONVERTER         ")
print("=========================================")

def ip_to_binary(ip):
    try:
        octets = ip.split('.')
        if len(octets) != 4:
            return "[!] Invalid IP format."
        
        bin_octets = [f"{int(octet):08b}" for octet in octets]
        return ".".join(bin_octets)
    except ValueError:
        return "[!] Invalid characters in IP."

ip_input = input("Enter an IPv4 Address (e.g., 192.168.1.1): ").strip()
binary_output = ip_to_binary(ip_input)

print("-----------------------------------------")
print(f"DECIMAL IP : {ip_input}")
print(f"BINARY IP  : {binary_output}")
print("-----------------------------------------")
print("CONVERSION COMPLETE. HOLD THE LINE.")
print("=========================================")