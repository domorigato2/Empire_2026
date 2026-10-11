import sys

def generate_port_security(int_range, max_macs=1, violation="shutdown"):
    print("\n==================================================================")
    print("      CISCO CCNA // AUTOMATED PORT SECURITY HARDENER              ")
    print("==================================================================")
    
    config = f"""! =======================================================
! CISCO IOS BULK PORT SECURITY PAYLOAD
! =======================================================
enable
configure terminal
!
interface range {int_range}
 switchport mode access
 switchport port-security
 switchport port-security maximum {max_macs}
 switchport port-security mac-address sticky
 switchport port-security violation {violation}
 no shutdown
exit
end
write memory
!
! Operational Verification:
! show port-security interface <INT>
! show port-security address
! ========================================================"""
    
    print(config)
    print("==================================================================\n")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        irange = sys.argv[1]
        max_m = sys.argv[2] if len(sys.argv) > 2 else 1
        viol = sys.argv[3] if len(sys.argv) > 3 else "shutdown"
        generate_port_security(irange, max_m, viol)
    else:
        print("[!] Usage: python cisco_port_security_gen.py <INT_RANGE> [MAX_MACS] [VIOLATION_MODE]")
        print("    Example: python cisco_port_security_gen.py fa0/1-24 1 shutdown")
