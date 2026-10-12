import datetime, os

def display_dashboard():
    now = datetime.datetime.now()
    interview_date = datetime.datetime(2026, 10, 13, 10, 30)
    time_left = interview_date - now
    
    hours, remainder = divmod(int(time_left.total_seconds()), 3600)
    minutes, _ = divmod(remainder, 60)
    
    print("\n" + "="*60)
    print(" ROOT KERNEL // EMPIRE 2026 OPERATIONAL DASHBOARD")
    print("="*60)
    print(f" OPERATOR       : Dominic Margherio | Node: Spring Valley")
    print(f" SYSTEM TIME     : {now.strftime('%Y-%m-%d %I:%M:%S %p')}")
    print("-" * 60)
    print(f" STREAKS        : Smoke-Free: 39d | Zero-Alc: 6d | Fasting: 69d")
    print(f" WAR CHEST      : $4.32 / $1,000.00 Target (PayPal)")
    print(f" DISPATCH CALL  : Monday Oct 12 @ 08:00 AM -> BPART (877-874-8813)")
    print(f" INTERVIEW NODE : Peru PADS (1320 Menards Dr, Peru, IL)")
    print(f" COUNTDOWN      : {hours}h {minutes}m remaining until interview")
    print("="*60 + "\n")

if __name__ == "__main__":
    display_dashboard()