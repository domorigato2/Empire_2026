print("=========================================")
print("       PAYPAL WAR CHEST ENGINE           ")
print("=========================================")

TARGET = 1000.00

# Input current capital
current_balance = float(input("Current PayPal Savings Balance ($): "))
today_earnings = float(input("Today's New Earnings to Deposit ($): "))

total_capital = current_balance + today_earnings
gap = TARGET - total_capital
percent = (total_capital / TARGET) * 100

# Visual progress bar
display_percent = min(percent, 100.0)
bar_length = 20
filled_length = int(bar_length * display_percent // 100)
bar = "█" * filled_length + "-" * (bar_length - filled_length)

print("-----------------------------------------")
print(f"ACTIVE CAPITAL : ${total_capital:.2f}")
print(f"REMAINING GAP  : ${gap:.2f}")
print(f"PROGRESS       : [{bar}] {percent:.1f}%")
print("-----------------------------------------")

if gap <= 0:
    print("OBJECTIVE COMPLETE. PHASE 2: INDEX INVESTING.")
else:
    lawns_needed = gap / 25.0
    print(f"MISSION GAP: Exactly {lawns_needed:.1f} lawns ($25) or daily microtasks to clear.")

print("=========================================")