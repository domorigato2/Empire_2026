import os
import sys
import datetime

DEVICES = {
    "SW-CORE-01": "hostname SW-CORE-01\nvlan 10 name MANAGEMENT\ninterface Vlan10\n ip address 192.168.10.1 255.255.255.0",
    "SW-DIST-02": "hostname SW-DIST-02\nvlan 30 name SERVER_FARM\ninterface Vlan30\n ip address 172.16.10.33 255.255.255.240",
    "RTR-PERU-01": "hostname RTR-PERU-01\ninterface GigabitEthernet0/0/0\n no shutdown\ninterface GigabitEthernet0/0/0.10\n encapsulation dot1Q 10\n ip address 192.168.10.1 255.255.255.0"
}

def backup_configs():
    print("\n==================================================")
    print("      NOC AUTOMATION // CONFIG BACKUP ENGINE      ")
    print("==================================================")
    print(" Initiating automated running-config pull...")
    print("--------------------------------------------------")

    backup_dir = "Backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    success_count = 0

    for dev_name, cfg in DEVICES.items():
        filename = f"{backup_dir}/{dev_name}_{timestamp}.cfg"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"! Backup generated on: {datetime.datetime.now()}\n")
                f.write(cfg)
            print(f" [+] BACKUP SUCCESS : {dev_name} --> {filename}")
            success_count += 1
        except Exception as e:
            print(f" [-] BACKUP FAILED  : {dev_name} --> Error: {e}")

    print("--------------------------------------------------")
    print(f" Backup Cycle Complete. Successful Pulls: {success_count}/{len(DEVICES)}")
    print("==================================================\n")

if __name__ == "__main__":
    backup_configs()
