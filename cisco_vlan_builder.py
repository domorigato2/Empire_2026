print("=========================================")
print("      CISCO IOS VLAN CONFIG BUILDER      ")
print("=========================================")

vlan_id = input("Enter VLAN ID (e.g., 10, 20, 99): ").strip()
vlan_name = input("Enter VLAN Name (e.g., MANAGEMENT, SALES): ").strip().upper()
int_range = input("Enter Access Interface Range (e.g., fa0/1 - 12): ").strip()

cisco_script = f"""enable
configure terminal
!
vlan {vlan_id}
 name {vlan_name}
 exit
!
interface range {int_range}
 switchport mode access
 switchport access vlan {vlan_id}
 no shutdown
 exit
!
do write memory
end
"""

print("\n-----------------------------------------")
print(cisco_script)
print("-----------------------------------------")

with open("cisco_deploy.txt", "w") as f:
    f.write(cisco_script)

print("[✓] CONFIG COMPILED & SAVED TO 'cisco_deploy.txt'.")
print("=========================================")