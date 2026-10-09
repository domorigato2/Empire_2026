import os
import sys
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_war_chest():
    log_file = "money.log"
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write("9.37")
        return 9.37
    try:
        with open(log_file, "r") as f:
            return float(f.read().strip())
    except ValueError:
        return 9.37

def update_war_chest(amount):
    log_file = "money.log"
    current = get_war_chest()
    new_total = current + amount
    with open(log_file, "w") as f:
        f.write(f"{new_total:.2f}")
    return new_total

def render_progress_bar(percentage, width=30):
    filled_len = int(width * percentage / 100)
    if filled_len == 0 and percentage > 0:
        filled_len = 1
    bar = '■' * filled_len + '░' * (width - filled_len)
    return f"[{bar}] {percentage:.4f}%"

def render_dashboard(current):
    target = 1000.00
    gap = target - current
    percentage = (current / target) * 100
    progress_bar = render_progress_bar(percentage)
    
    clear_screen()
    print("==================================================================")
    print("        DOMINIC EMPIRE // ALL-OPTIMIZATION HUD v1.3               ")
    print("==================================================================")
    print(f" [^] War Chest Target   : ${target:.2f}")
    print(f" [^] Liquid Capital     : ${current:.2f}")
    print(f" [^] Remaining Deficit  : ${gap:.2f}")
    print(f" [^] Visual Progress    : {progress_bar}")
    print("------------------------------------------------------------------")
    print(f" [^] Chassis Status     : Bed Turret (Hydrostatic Drain Active)")
    print(f" [^] Audio Shield       : Anker Soundcore Q30 (Acoustic / ANC)")
    print(f" [^] Nicotine Firewall  : Day 36 (0.0% Tolerance)")
    print(f" [^] Alcohol Detox      : Day 5 (Librium 12h Taper Active)")
    print(f" [^] Next Pharmacological Lock : 07:00 PM STRICT")
    print(f" [^] System Timestamp   : {time.strftime('%I:%M %p // %Y-%m-%d')}")
    print("==================================================================")
    print(" STATUS: SYSTEM RUNNING AT PEAK SIGNAL. ZERO DROPPED PACKETS.    ")
    print("==================================================================")

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            try:
                delta = float(sys.argv[1])
                new_val = update_war_chest(delta)
                print(f"[+] Transaction logged: ${delta:+.2f} -> New Total: ${new_val:.2f}")
                time.sleep(1.2)
            except ValueError:
                print("[!] Error: Invalid monetary value passed to CLI.")
        
        current_capital = get_war_chest()
        render_dashboard(current_capital)
    except KeyboardInterrupt:
        print("\n[!] Terminal session terminated by Operator.")
        sys.exit(0)
