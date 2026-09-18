import datetime

print("=========================================")
print("      ROOT OPERATOR TELEMETRY v2.0       ")
print("=========================================")

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Ceiling config
CEILING = 15

# Operator Inputs
beers_in = input("Beers consumed today: ")
cigs_in = input("Cigarettes consumed: ")
capital_in = input("Micro-capital earned today ($): ")

# Data conversion & Math
beers = int(beers_in)
cigs = int(cigs_in)
remaining = CEILING - beers

# System Logic Gates
if remaining > 0:
    status = f"STABLE | {remaining} UNITS REMAINING"
elif remaining == 0:
    status = "MAX REACHED | VALVE WELDED SHUT"
else:
    status = f"OVERFLOW BREACH | {abs(remaining)} UNITS OVER"

# Print instant telemetry to screen
print("-----------------------------------------")
print(f"SYSTEM STATUS: {status}")
if cigs == 0:
    print("NICOTINE FIREWALL: 0.0% (DAY 15 HOLDING)")
else:
    print(f"NICOTINE BREACH: {cigs} PUFFS DETECTED")
print("-----------------------------------------")

# Format and append payload to vault
payload = f"[{now}] Consumed: {beers}/{CEILING} | Ammo Left: {remaining} | Cigs: {cigs} | Capital: ${capital_in} | Status: {status}\n"

with open("telemetry_vault.txt", "a") as file:
    file.write(payload)

print("DATA COMMITTED TO VAULT. DISCIPLINE IS FREEDOM.")
print("=========================================")