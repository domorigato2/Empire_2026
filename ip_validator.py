import sys

def validate_ipv4(ip_string):
    octets = ip_string.split(".")
    
    # Must have exactly 4 octets
    if len(octets) != 4:
        return False, "Packet Drop: IP must contain exactly 4 octets."
        
    for octet in octets:
        # Check if digits only
        if not octet.isdigit():
            return False, f"Packet Drop: Non-numeric octet detected ('{octet}')."
            
        val = int(octet)
        # Check boundary 0-255
        if val < 0 or val > 255:
            return False, f"Buffer Overflow: Octet '{val}' out of bounds (0-255)."
            
    return True, "Packet Verified: Valid IPv4 Host/Network Address."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_ip = sys.argv[1]
        is_valid, msg = validate_ipv4(target_ip)
        
        print("\n========================================")
        print("     CISCO CCNA // IPv4 PACKET CHECK    ")
        print("========================================")
        print(f" Target IP : {target_ip}")
        print(f" Status    : {'[VALID]' if is_valid else '[CORRUPT]'}")
        print(f" Telemetry : {msg}")
        print("========================================\n")
    else:
        print("[!] Usage: python ip_validator.py <IP_ADDRESS>")
