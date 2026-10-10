import random
import sys
import os

QUESTIONS = [
    {
        "q": "What is the default administrative distance of OSPF?",
        "options": ["A) 90", "B) 110", "C) 120", "D) 0"],
        "answer": "B"
    },
    {
        "q": "Which OSI layer handles reliable end-to-end data delivery and flow control?",
        "options": ["A) Layer 2 (Data Link)", "B) Layer 3 (Network)", "C) Layer 4 (Transport)", "D) Layer 7 (Application)"],
        "answer": "C"
    },
    {
        "q": "What command displays the active MAC address table on a Cisco Catalyst switch?",
        "options": ["A) show ip route", "B) show mac address-table", "C) show interfaces trunk", "D) show arp"],
        "answer": "B"
    },
    {
        "q": "Which IPv6 address type is routable only on a single local link and is never routed across the internet?",
        "options": ["A) Global Unicast", "B) Unique Local", "C) Link-Local", "D) Multicast"],
        "answer": "C"
    },
    {
        "q": "What is the primary function of Spanning Tree Protocol (STP)?",
        "options": ["A) Encrypt VLAN traffic", "B) Prevent Layer 2 switching loops", "C) Assign dynamic IP addresses", "D) Load balance WAN links"],
        "answer": "B"
    },
    {
        "q": "What port number does SSH use by default?",
        "options": ["A) 21", "B) 23", "C) 22", "D) 80"],
        "answer": "C"
    },
    {
        "q": "Which VLAN range is reserved for VLAN IDs 1006 through 4094 and does not save configurations to vlan.dat?",
        "options": ["A) Normal Range", "B) Extended Range", "C) Native Range", "D) Reserved Range"],
        "answer": "B"
    }
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_drill():
    score = 0
    total = len(QUESTIONS)
    
    clear()
    print("==================================================")
    print("     CISCO CCNA 200-301 // TERMINAL DRILL ENGINE  ")
    print("==================================================")
    print(f" Loaded {total} high-yield core networking questions.\n")
    
    for idx, item in enumerate(random.sample(QUESTIONS, total), 1):
        print(f" [Q{idx}] {item['q']}")
        for opt in item['options']:
            print(f"   {opt}")
        ans = input(" [>] Your Answer (A/B/C/D): ").strip().upper()
        if ans == item['answer']:
            print(" [+] STATUS: CORRECT.\n")
            score += 1
        else:
            print(f" [-] STATUS: INCORRECT. Correct answer was {item['answer']}.\n")
            
    print("==================================================")
    print(f" DRILL COMPLETE. Score: {score}/{total} ({int((score/total)*100)}%)")
    print("==================================================\n")

if __name__ == "__main__":
    run_drill()
