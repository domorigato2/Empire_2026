import sys

def calculate_runway(current_funds, daily_earnings):
    target = 1000.00
    deficit = target - current_funds
    
    print("\n==================================================")
    print("      WAR CHEST // CAPITAL RUNWAY CALCULATOR      ")
    print("==================================================")
    print(f" Current Capital : ${current_funds:.2f}")
    print(f" Target Goal     : ${target:.2f}")
    print(f" Remaining Gap   : ${deficit:.2f}")
    print(f" Projected Rate  : ${daily_earnings:.2f} / day")
    print("--------------------------------------------------")
    
    if daily_earnings > 0:
        days_to_target = deficit / daily_earnings
        print(f" [+] Time to Target: {days_to_target:.1f} Days (~{days_to_target/30:.1f} Months)")
    else:
        print(" [-] Rate is zero. Capital stagnation detected.")
    print("==================================================\n")

if __name__ == "__main__":
    funds = float(sys.argv[1]) if len(sys.argv) > 1 else 9.37
    rate = float(sys.argv[2]) if len(sys.argv) > 2 else 5.00
    calculate_runway(funds, rate)
