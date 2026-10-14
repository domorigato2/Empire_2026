# ==========================================
# APEX PYTHON IPV4 SUBNET CALCULATOR
# CCNA Automated Logic Engine
# ==========================================

import sys

def calculate_subnet(cidr):
    try:
        # Split IP and prefix length (e.g., "192.168.1.135/27")
        ip_part, prefix_part = cidr.split('/')
        prefix = int(prefix_part)
        
        if not (0 <= prefix <= 32):
            print("[-] Error: CIDR prefix must be between 0 and 32.")
            return

        # Calculate Block Size (Magic Number) in the 4th octet (assuming /24 to /32 range)
        # For simplicity in this base tool, we look at the host bits remaining in the 4th octet:
        host_bits = 32 - prefix
        block_size = 2 ** host_bits if host_bits <= 8 else 256 # Simplified for last octet
        total_hosts = (2 ** host_bits) - 2 if host_bits > 1 else (2 ** host_bits)
        
        octets = ip_part.split('.')
        target_last_octet = int(octets[3])
        
        # Find network ID block
        net_id_last = (target_last_octet // block_size) * block_size
        broadcast_last_octet = net_id_last + block_size - 1
        
        print("\n" + "="*40)
        print(f"[*] TARGET IP:       {ip_part} (CIDR: /{prefix})")
        print(f"[*] BLOCK SIZE:      {block_size}")
        print(f"[*] NETWORK ID:      {octets[0]}.{octets[1]}.{octets[2]}.{net_id_last}")
        print(f"[*] USABLE RANGE:    {octets[0]}.{octets[1]}.{octets[2]}.{net_id_last + 1}  THROUGH  {octets[0]}.{octets[1]}.{octets[2]}.{broadcast_last_octet - 1}")
        print(f"[*] BROADCAST IP:    {octets[0]}.{octets[1]}.{octets[2]}.{broadcast_last_octet}")
        print(f"[*] TOTAL HOSTS:     {max(0, total_hosts)}")
        print("="*40 + "\n")

    except Exception as e:
        print(f"[-] Malformed input packet: {e}")

if __name__ == "__main__":
    print("\n--- CCNA AUTOMATED SUBNET ENGINE ---")
    user_input = input("Enter IP with CIDR (e.g., 192.168.1.135/27): ").strip()
    calculate_subnet(user_input)