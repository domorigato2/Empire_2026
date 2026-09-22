#!/usr/bin/env python3
# bingo_calc.py - Dominic Empire OS

print("--- BINGO CLASH P-LEVEL CALCULATOR ---")
current_p7 = int(input("Enter your current P7 points (e.g., 12800): "))
target_p7 = 30000
points_per_game = 6

games_per_day = int(input("How many $0.60 games do you play a day? "))

points_needed = target_p7 - current_p7
games_needed = points_needed / points_per_game
days_needed = games_needed / games_per_day

print("-" * 40)
print(f"Points needed for P8: {points_needed}")
print(f"Total $0.60 games required: {int(games_needed)}")
print(f"At {games_per_day} games/day, you will hit P8 in {round(days_needed, 1)} days.")
print("-" * 40)