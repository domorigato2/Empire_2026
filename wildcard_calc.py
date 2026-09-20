print("=========================================")
print("      CCNA WILDCARD MASK CALCULATOR      ")
print("=========================================")

subnet_mask = input("Enter Subnet Mask (e.g., 255.255.255.240): ").strip()

try:
    octets = subnet_mask.split('.')
    if len(octets) != 4:
        print("[!] Invalid format. Must be 4 octets.")
    else:
        wildcard = []
        for octet in octets:
            # Wildcard is 255 - subnet mask octet
            wild_octet = 255 - int(octet)
            if wild_octet < 0 or wild_octet > 255:
                raise ValueError
            wildcard.append(str(wild_octet))
            
        wildcard_mask = ".".join(wildcard)
        
        print("\n-----------------------------------------")
        print(f"SUBNET MASK   : {subnet_mask}")
        print(f"WILDCARD MASK : {wildcard_mask}")
        print("-----------------------------------------")
        print("[*] CCNA NOTE: Wildcard masks are used in OSPF and ACLs.")
        print("    0 = Match exactly, 255 = Ignore (Any).")
        print("=========================================")
except ValueError:
    print("\n[!] Invalid numbers in mask. Use 0-255.")