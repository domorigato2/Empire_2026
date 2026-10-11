import sys

def generate_vlan_db(vlan_data):
    print("\n==================================================")
    print("      CISCO CCNA // VLAN DATABASE AUTOMATOR       ")
    print("==================================================")
    
    config = "! [VLAN DATABASE PAYLOAD]\n"
    config += "enable\nconfigure terminal\n!\n"
    
    # Input format: ID:Name,ID:Name (e.g. 10:MGMT,20:DATA)
    pairs = vlan_data.split(',')
    for pair in pairs:
        v_id, v_name = pair.split(':')
        config += f"vlan {v_id}\n name {v_name.upper()}\nexit\n"
        
    config += "!\nend\nwrite memory\n"
    print(config)
    print("==================================================\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        generate_vlan_db(sys.argv[1])
    else:
        print("[!] Usage: python vlan_db_gen.py <ID:NAME,ID:NAME,...>")
        print("    Example: python vlan_db_gen.py 10:MGMT,20:DATA,30:VOICE")
