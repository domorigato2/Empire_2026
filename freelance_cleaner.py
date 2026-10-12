# Save as freelance_cleaner.py in C:\Users\sheil\Empire_2026\
import csv
import re

def clean_client_data(input_data):
    print("\n" + "="*60)
    print(" FREELANCE AUTOMATION // DATA CLEANSING ENGINE")
    print("="*60)
    
    cleaned_records = []
    seen_emails = set()
    
    for row in input_data:
        name = row.get("Name", "").strip().title()
        email = row.get("Email", "").strip().lower()
        phone = row.get("Phone", "").strip()
        
        # 1. Validate Email via Regex
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            print(f" [X] Dropped Invalid Email: {email}")
            continue
            
        # 2. Drop Duplicates based on Email
        if email in seen_emails:
            print(f" [!] Dropped Duplicate Record: {email}")
            continue
        seen_emails.add(email)
        
        # 3. Format Phone Number (Standardize to XXX-XXX-XXXX if digits match)
        digits = re.sub(r'\D', '', phone)
        if len(digits) == 10:
            formatted_phone = f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
        else:
            formatted_phone = phone # Keep raw if international or malformed
            
        cleaned_records.append({
            "Name": name,
            "Email": email,
            "Phone": formatted_phone,
            "Status": "Verified"
        })
        
    print("-" * 60)
    print(f" [+] Success: {len(cleaned_records)} clean records processed.")
    print("="*60 + "\n")
    return cleaned_records

if __name__ == "__main__":
    # Simulate messy client input payload
    messy_input = [
        {"Name": "dominic margherio", "Email": "d.margherio@domain.com", "Phone": "(309) 555-0199"},
        {"Name": "test user", "Email": "user@com", "Phone": "5550192"}, # Invalid email
        {"Name": "Dominic Margherio", "Email": "D.Margherio@domain.com", "Phone": "309-555-0199"}, # Duplicate
        {"Name": "jane doe", "Email": "jane.doe@enterprise.org", "Phone": "3125550144"}
    ]
    
    clean_client_data(messy_input)