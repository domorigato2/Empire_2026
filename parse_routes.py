import re

cisco_route_dump = """
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 

Gateway of last resort is 192.168.1.1 to network 0.0.0.0

S*    0.0.0.0/0 [1/0] via 192.168.1.1
C     10.10.10.0/24 is directly connected, GigabitEthernet0/0
L     10.10.10.1/32 is directly connected, GigabitEthernet0/0
O     172.16.0.0/16 [110/20] via 10.10.10.2, 00:14:22, GigabitEthernet0/0
D     192.168.20.0/24 [90/307200] via 10.10.10.3, 01:02:15, GigabitEthernet0/1
"""

def parse_ios_routes(raw_dump):
    print("\n" + "="*60)
    print(" CISCO ROUTING TELEMETRY // PARSED INTERFACES")
    print("="*60)
    
    pattern = r'([A-Z][\*]?)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})\s+(.*)'
    routes = re.findall(pattern, raw_dump)
    
    proto_map = {
        'C': 'CONNECTED',
        'L': 'LOCAL',
        'S': 'STATIC',
        'S*': 'DEFAULT STATIC',
        'O': 'OSPF',
        'D': 'EIGRP'
    }
    
    for proto, prefix, details in routes:
        protocol_name = proto_map.get(proto, proto)
        print(f"[{protocol_name:<14}] {prefix:<18} -> {details}")
        
    print("="*60 + "\n")

if __name__ == "__main__":
    parse_ios_routes(cisco_route_dump)