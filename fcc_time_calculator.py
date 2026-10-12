# Save as fcc_time_calculator.py in C:\Users\sheil\Empire_2026\

def add_time(start, duration, day_of_week=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Parse start time
    start_time, period = start.split()
    start_hour, start_min = map(int, start_time.split(':'))
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0
        
    # Parse duration
    dur_hour, dur_min = map(int, duration.split(':'))
    
    total_min = start_min + dur_min
    extra_hour = total_min // 60
    final_min = total_min % 60
    
    total_hour = start_hour + dur_hour + extra_hour
    days_later = total_hour // 24
    final_hour_24 = total_hour % 24
    
    # Convert back to 12-hour format
    final_period = "AM" if final_hour_24 < 12 else "PM"
    final_hour_12 = final_hour_24 % 12
    if final_hour_12 == 0:
        final_hour_12 = 12
        
    min_str = f"{final_min:02d}"
    result = f"{final_hour_12}:{min_str} {final_period}"
    
    if day_of_week:
        lower_days = [d.lower() for d in days_of_week]
        start_index = lower_days.index(day_of_week.lower())
        new_day_index = (start_index + days_later) % 7
        result += f", {days_of_week[new_day_index]}"
        
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"
        
    return result

if __name__ == "__main__":
    print("\n" + "="*50)
    print(" FREECODECAMP TIME CALCULATOR ENGINE")
    print("="*50)
    print(" [+] Test 1:", add_time("3:00 PM", "3:10"))
    print(" [+] Test 2:", add_time("11:30 AM", "2:32", "Monday"))
    print(" [+] Test 3:", add_time("11:43 PM", "24:20", "tuesday"))
    print("="*50 + "\n")