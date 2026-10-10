import sys

TICKET_STORE = [
    {"name": "$0.10 Bonus (Exclusive)", "tickets": 2200, "cash": 0.10},
    {"name": "$0.50 Bonus (Exclusive)", "tickets": 10000, "cash": 0.50},
    {"name": "$1.00 Bonus (Regular)",   "tickets": 19000, "cash": 1.00},
    {"name": "$2.00 Bonus (Regular)",   "tickets": 34000, "cash": 2.00},
    {"name": "$5.00 Bonus (Regular)",   "tickets": 75000, "cash": 5.00},
    {"name": "$10.00 Bonus (Exclusive)","tickets": 145000, "cash": 10.00},
]

def analyze_bingo(current_tickets, daily_box_rate=1000):
    print("\n==================================================================")
    print("      BINGO CLASH // TICKET EXCHANGE EFFICIENCY CALCULATOR        ")
    print("==================================================================")
    print(f" Current Ticket Reserve : {current_tickets:,}")
    print(f" Daily Passive Accrual  : ~{daily_box_rate:,} tickets/day (5x Lucky Boxes)")
    print("------------------------------------------------------------------")
    print(f" {'STORE ITEM':<26} | {'COST':<7} | {'EFFICIENCY':<12} | {'WAIT TIME'}")
    print("-" * 66)
    
    for item in TICKET_STORE:
        cost = item["tickets"]
        cash = item["cash"]
        eff = cost / cash  # Tickets per dollar (lower is better value)
        gap = max(0, cost - current_tickets)
        days = gap / daily_box_rate if daily_box_rate > 0 else 0
        
        print(f" {item['name']:<26} | {cost:>6,} | {eff:>6,.0f} tix/$ | {days:>5.1f} days")
        
    print("==================================================================")
    print(" STRATEGY: Target the 10k ($0.50) or 19k ($1.00) tier.")
    print(" Farm $0.60 games. Never sit in 5-month ticket purgatory.")
    print("==================================================================\n")

if __name__ == "__main__":
    current = int(sys.argv[1]) if len(sys.argv) > 1 else 2671
    analyze_bingo(current)
