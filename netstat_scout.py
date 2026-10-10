import subprocess
import sys

def parse_netstat():
    print("\n==================================================")
    print("      ACTIVE SOCKET SCOUT // NETSTAT PARSER       ")
    print("==================================================")
    print(" Querying OS kernel network socket table...")
    print("--------------------------------------------------")

    cmd = ["netstat", "-ano"]
    try:
        output = subprocess.check_output(cmd, universal_newlines=True)
    except Exception as e:
        print(f"[!] Netstat Execution Failed: {e}")
        return

    listening_count = 0
    established_count = 0

    print(f" {'PROTO':<6} | {'LOCAL ADDRESS':<22} | {'FOREIGN ADDRESS':<22} | {'STATE':<12} | {'PID'}")
    print("-" * 80)

    for line in output.splitlines():
        parts = line.strip().split()
        if len(parts) >= 4:
            proto = parts[0]
            if proto in ["TCP", "UDP"]:
                local = parts[1]
                foreign = parts[2] if len(parts) > 2 else "N/A"
                
                # Handle TCP state vs UDP lack of state
                if proto == "TCP":
                    state = parts[3] if len(parts) > 3 else "N/A"
                    pid = parts[4] if len(parts) > 4 else "N/A"
                else:
                    state = "LISTENING"
                    pid = parts[3] if len(parts) > 3 else "N/A"

                if proto == "TCP" and state == "LISTENING":
                    listening_count += 1
                elif proto == "TCP" and state == "ESTABLISHED":
                    established_count += 1

                # Print key operational states
                if proto == "TCP" and (state == "ESTABLISHED" or state == "LISTENING"):
                    print(f" {proto:<6} | {local:<22} | {foreign:<22} | {state:<12} | {pid}")

    print("-" * 80)
    print(f" Active TCP Listening Sockets : {listening_count}")
    print(f" Active TCP Established Links : {established_count}")
    print("==================================================\n")

if __name__ == "__main__":
    parse_netstat()
