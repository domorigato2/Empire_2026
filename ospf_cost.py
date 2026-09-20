print("=========================================")
print("       CCNA OSPF COST CALCULATOR         ")
print("=========================================")

print("Default Cisco Reference Bandwidth: 100 Mbps")
ref_bw_input = input("Enter Reference Bandwidth in Mbps (Press Enter for 100): ").strip()

if not ref_bw_input:
    ref_bw = 100
else:
    ref_bw = int(ref_bw_input)

int_bw_input = input("Enter Interface Bandwidth in Mbps (e.g., 10, 100, 1000): ").strip()
int_bw = int(int_bw_input)

# OSPF Cost formula: Reference BW / Interface BW (Minimum cost is 1)
cost = max(1, int(ref_bw / int_bw))

print("\n-----------------------------------------")
print(f"REFERENCE BANDWIDTH : {ref_bw} Mbps")
print(f"INTERFACE BANDWIDTH : {int_bw} Mbps")
print(f"OSPF METRIC (COST)  : {cost}")
print("-----------------------------------------")
print("[*] CCNA NOTE: OSPF uses Cost as its metric. Lower cost = preferred route.")
print("[*] CCNA TRAP: If Cost = 1 for both FastEthernet and Gigabit, you must")
print("    change the reference bandwidth using 'auto-cost reference-bandwidth'.")
print("=========================================")