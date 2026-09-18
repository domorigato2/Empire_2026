import datetime

print("=========================================")
print("       ROOT OPERATOR STREAK VAULT        ")
print("=========================================")

streaks = {
    "Nicotine-Free (0.0% Tolerance)": "Day 15 (Record Shattered)",
    "Daily Steps (20,000 / 4 Hours)": "Day 6 Active",
    "2x Daily Cold Showers & Baking Soda": "Day 4 Active",
    "Zero-Carb / Egg & Sardine Protocol": "Day 47 Active",
    "AI Integration & Terminal Grind": "Day 6 Active",
    "Spanish Acquisition (Duolingo)": "Day 1 Rebooted"
}

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print(f"TELEMETRY AUDIT AS OF: {now}\n")

for habit, streak in streaks.items():
    print(f" [*] {habit:<35} : {streak}")

print("-----------------------------------------")
print("MISSION: SHIPIBO AYAHUASCA DIETA (2027)")
print("LOCATION: NIHUE RAO | STATUS: HARDENING NODE")
print("=========================================")