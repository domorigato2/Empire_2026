import subprocess
import sys

def hunt_processes():
    print("\n==================================================")
    print("      PROCESS HUNTER // TASKLIST PARSER           ")
    print("==================================================")
    print(" Querying OS process execution table...")
    print("--------------------------------------------------")

    cmd = ["tasklist", "/FO", "CSV"]
    try:
        output = subprocess.check_output(cmd, universal_newlines=True)
    except Exception as e:
        print(f"[!] Tasklist Execution Failed: {e}")
        return

    lines = output.strip().splitlines()
    print(f" {'IMAGE NAME':<25} | {'PID':<8} | {'SESSION NAME':<12} | {'MEM USAGE'}")
    print("-" * 75)

    # Skip CSV header line
    for line in lines[1:]:
        parts = line.replace('"', '').split(',')
        if len(parts) >= 5:
            name = parts[0]
            pid = parts[1]
            session = parts[2]
            mem = parts[4]
            print(f" {name:<25} | {pid:<8} | {session:<12} | {mem}")

    print("-" * 75)
    print(f" Total Active Processes Mapped: {len(lines) - 1}")
    print("==================================================\n")

if __name__ == "__main__":
    hunt_processes()
