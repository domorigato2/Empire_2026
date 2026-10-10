import sys

def generate_nat_pat(inside_net, inside_wildcard, inside_int, outside_int, acl_num=1):
    print("\n==================================================================")
    print("     CISCO CCNA // NAT OVERLOAD (PAT) AUTOMATION ARCHITECT        ")
    print("==================================================================")

    config = f"""! =======================================================
! CISCO IOS NAT OVERLOAD (PAT) PAYLOAD
! =======================================================
enable
configure terminal
!
! [1] Define standard ACL matching inside private RFC 1918 traffic
access-list {acl_num} permit {inside_net} {inside_wildcard}
!
! [2] Configure dynamic PAT overload mapping to public exit interface
ip nat inside source list {acl_num} interface {outside_int} overload
!
! [3] Designate inside (LAN) and outside (WAN/ISP) interfaces
interface {inside_int}
 description Inside LAN Network ({inside_net})
 ip nat inside
exit
!
interface {outside_int}
 description Outside WAN/ISP Uplink
 ip nat outside
exit
!
end
write memory
!
! Operational Verification:
! show ip nat translations
! show ip nat statistics
! clear ip nat translation *"""

    print(config)
    print("==================================================================\n")

if __name__ == "__main__":
    if len(sys.argv) >= 5:
        in_net = sys.argv[1]
        in_wild = sys.argv[2]
        in_int = sys.argv[3]
        out_int = sys.argv[4]
        acl = sys.argv[5] if len(sys.argv) > 5 else 1
        generate_nat_pat(in_net, in_wild, in_int, out_int, acl)
    else:
        print("[!] Usage: python cisco_nat_gen.py <INSIDE_NET> <WILDCARD> <INSIDE_INT> <OUTSIDE_INT> [ACL_NUM]")
        print("    Example: python cisco_nat_gen.py 192.168.10.0 0.0.0.255 G0/0/0 G0/0/1 1")
