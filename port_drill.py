import random
import sys

def run_port_drill():
    print("=========================================")
    print("      CCNA WELL-KNOWN PORTS SPEED DRILL  ")
    print("=========================================")
    print("Goal: Enter the correct Layer 4 Port Number.\n")

    protocols = {
        "SSH (Secure Shell)": "22",
        "Telnet (Unencrypted CLI)": "23",
        "DNS (Domain Name System)": "53",
        "DHCP Server": "67",
        "HTTP (Web Plaintext)": "80",
        "HTTPS (Web Encrypted)": "443",
        "NTP (Network Time Protocol)": "123",
        "SNMP (Simple Network Mgmt)": "161"
    }

    items = list(protocols.items())
    random.shuffle(items)
    
    score = 0
    rounds = 4

    for i in range(1, rounds + 1):
        proto, correct_port = items[i - 1]
        print(f"[ROUND {i}/{rounds}] PROTOCOL: {proto}")
        user_ans = input("Enter Port Number: ").strip()
        
        if user_ans == correct_port:
            print(f" [✓] CORRECT! Port is {correct_port}.\n")
            score += 1
        else:
            print(f" [✗] INCORRECT. Correct Port was: {correct_port}\n")

    print("-----------------------------------------")
    print(f"DRILL COMPLETE | SCORE: {score}/{rounds} ({(score/rounds)*100:.0f}%)")
    if score == rounds:
        print("STATUS: LAYER 4 PORT REFLEXES OPTIMIZED.")
    else:
        print("STATUS: REVIEW FAILED PORTS IN CCNA FLASHCARDS.")
    print("=========================================")

if __name__ == "__main__":
    run_port_drill()