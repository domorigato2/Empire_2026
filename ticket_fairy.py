#!/usr/bin/env python3
# ticket_fairy.py - Dominic Empire OS

import datetime

print("--- BINGO CLASH TICKET FAIRY ---")
cooldown_hours = float(input("How many hours between lucky boxes? (e.g., 4 or 4.5): "))

now = datetime.datetime.now()
print(f"\nCurrent Time: {now.strftime('%I:%M %p')}")
print("-" * 40)

for i in range(1, 6):
    next_time = now + datetime.timedelta(hours=cooldown_hours * i)
    print(f"Box {i} Collection Time: {next_time.strftime('%I:%M %p')}")
print("-" * 40)