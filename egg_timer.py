import time
import sys

def egg_timer(seconds=420):
    print("\n[+] EGG TIMER ACTIVE // 7.0 MINUTE COUNTDOWN ENGAGED")
    print("--------------------------------------------------")
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        time_str = f"{mins:02d}:{secs:02d}"
        sys.stdout.write(f"\r [!] TIME UNTIL EGG EXTRACTION: {time_str} ")
        sys.stdout.flush()
        time.sleep(1)
    
    print("\n\n" + "=" * 50)
    print(" [***] TIMER EXPIRED! EXTRACT EGGS FROM HEAT NOW! [***]")
    print("=" * 50 + "\n")
    # Terminal bell alert
    print("\a\a\a")

if __name__ == "__main__":
    duration = int(sys.argv[1]) if len(sys.argv) > 1 else 420
    egg_timer(duration)
