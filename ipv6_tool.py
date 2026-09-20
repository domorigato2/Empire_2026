import ipaddress

print("=========================================")
print("      CCNA IPv6 COMPRESSOR & EXPANDER    ")
print("=========================================")

raw_ipv6 = input("Enter an IPv6 Address: ").strip()

try:
    # Parse IPv6 using standard library
    addr = ipaddress.IPv6Address(raw_ipv6)
    
    compressed = addr.compressed
    exploded = addr.exploded
    
    print("\n-----------------------------------------")
    print(f"RAW INPUT   : {raw_ipv6}")
    print(f"COMPRESSED  : {compressed}")
    print(f"EXPLODED    : {exploded}")
    print("-----------------------------------------")
    print(f"IS LOOPBACK : {addr.is_loopback}")
    print(f"IS LINK-LOCAL: {addr.is_link_local}")
    print("-----------------------------------------")
    print("[*] CCNA NOTE: '::' can only be used ONCE per address.")
    print("    Leading zeros in any 16-bit block can always be dropped.")
    print("=========================================")

except ValueError as err:
    print(f"\n[!] Invalid IPv6 syntax: {err}")
    print("=========================================")