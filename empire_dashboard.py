import os
import sys
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_war_chest():
    log_file = "Config/money.log" if os.path.exists("Config/money.log") else "money.log"
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write("9.37")
        return 9.37
    try:
        with open(log_file, "r") as f:
            return float(f.read().strip())
    except ValueError:
        return 9.37

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
    print("        DOMINIC EMPIRE // ALL-OPTIMIZATION HUD v1.4               ")
    print("==================================================================")
    print(f" [^] War Chest Target   : ${target:.2f}")
    print(f" [^] Liquid Capital     : ${current:.2f}")
    print(f" [^] Remaining Deficit  : ${gap:.2f}")
    print(f" [^] Visual Progress    : {progress_bar}")
    print("------------------------------------------------------------------")
    print(f" [^] Chassis Weight     : 117.6 lbs (+6.6 lbs Surge // Hydrated)")
    print(f" [^] Chassis Status     : Bed Turret (Hydrostatic Drain Active)")
    print(f" [^] Nicotine Firewall  : Day 39 (0.0% Tolerance)")
    print(f" [^] Alcohol Detox      : Day 6 (Librium 12h Taper Active)")
    print(f" [^] Next Pharma Lock   : 07:00 AM STRICT (Morning Payload)")
    print(f" [^] System Timestamp   : {time.strftime('%I:%M %p // %Y-%m-%d')}")
    print("==================================================================")
    print(" STATUS: RECOVERY RUNWAY EXPANDED. CODE REPOSITORY ACTIVE.       ")
    print("==================================================================")

if __name__ == "__main__":
    current_capital = get_war_chest()
    render_dashboard(current_capital)
