import subprocess
import sys
import time
import datetime
import os

def monitor_host(target, interval=3, count=5):
    print("\n==================================================")
    print("      NOC AUTOMATION // CONTINUOUS UPTIME MONITOR ")
    print("==================================================")
    print(f" Target Host : {target}")
    print(f" Interval    : {interval} seconds")
    print(f" Iterations  : {count} cycles")
    print("--------------------------------------------------")

    # Ensure Config directory exists for logging
    if not os.path.exists("Config"):
        os.makedirs("Config")
    log_file = "Config/uptime.log"
    
    for i in range(1, count + 1):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cmd = ["ping", "-n", "1", "-w", "1000", target]
        
        res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        is_up = (res.returncode == 0)
        
        status_str = "[ONLINE]" if is_up else "[OFFLINE]"
        log_line = f"[{timestamp}] HOST: {target} | STATUS: {status_str}\n"
        
        print(f" [{i:02d}] {timestamp} --> {target} : {status_str}")
        
        with open(log_file, "a") as f:
            f.write(log_line)
            
        if i < count:
            time.sleep(interval)

    print("--------------------------------------------------")
    print(f" Monitoring Session Complete. Results logged to {log_file}")
    print("==================================================\n")

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "1.1.1.1"
    cnt = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    monitor_host(host, 3, cnt)
