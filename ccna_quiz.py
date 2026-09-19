import sys

def run_quiz():
    print("=========================================")
    print("        CCNA 200-301 TERMINAL DRILL      ")
    print("=========================================")

    questions = [
        {
            "q": "1. At which OSI layer does a standard router operate?",
            "options": ["A) Layer 1 (Physical)", "B) Layer 2 (Data Link)", "C) Layer 3 (Network)", "D) Layer 4 (Transport)"],
            "answer": "C"
        },
        {
            "q": "2. What is the broadcast address for the network 192.168.1.0/24?",
            "options": ["A) 192.168.1.0", "B) 192.168.1.254", "C) 192.168.1.255", "D) 192.168.2.1"],
            "answer": "C"
        },
        {
            "q": "3. How many USABLE host IP addresses exist in a /30 point-to-point subnet?",
            "options": ["A) 1", "B) 2", "C) 4", "D) 6"],
            "answer": "B"
        },
        {
            "q": "4. Which protocol does the 'ping' command use to verify Layer 3 reachability?",
            "options": ["A) TCP", "B) UDP", "C) ARP", "D) ICMP"],
            "answer": "D"
        },
        {
            "q": "5. What is the standard administrative distance (AD) of OSPF?",
            "options": ["A) 90", "B) 110", "C) 120", "D) 1"],
            "answer": "B"
        }
    ]

    score = 0
    total = len(questions)

    for item in questions:
        print(f"\n{item['q']}")
        for opt in item['options']:
            print(f"   {opt}")
        user_ans = input("Your Answer (A/B/C/D): ").strip().upper()
        
        if user_ans == item['answer']:
            print("   [✓] CORRECT. Packet delivered.")
            score += 1
        else:
            print(f"   [✗] INCORRECT. Correct answer was {item['answer']}.")

    print("\n-----------------------------------------")
    print(f"DRILL COMPLETE | SCORE: {score}/{total} ({(score/total)*100:.0f}%)")
    if score == total:
        print("STATUS: MASTER OPERATOR. ZERO PACKET LOSS.")
    else:
        print("STATUS: REVIEW FAILED PACKETS IN JEREMY'S IT LAB.")
    print("=========================================")

if __name__ == "__main__":
    run_quiz()