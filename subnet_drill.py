import ipaddress
import random
import sys

def run_subnet_drill():
    print("=========================================")
    print("      CCNA IPv4 SUBNET SPEED DRILL       ")
    print("=========================================")
    print("Goal: Enter the correct Network ID for the target.\n")

    rounds = 3
    score = 0

    for i in range(1, rounds + 1):
        # Generate random Class C private subnet
        third_octet = random.randint(1, 254)
        fourth_octet = random.randint(1, 254)
        cidr = random.randint(25, 30) # High-yield CCNA masks
        
        target_str = f"192.168.{third_octet}.{fourth_octet}/{cidr}"
        
        # Calculate ground truth
        network_obj = ipaddress.ip_network(target_str, strict=False)
        correct_net_id = str(network_obj.network_address)
        
        print(f"[ROUND {i}/{rounds}] TARGET HOST: {target_str}")
        print(f"Mask: {network_obj.netmask} | Block Size: {network_obj.num_addresses}")
        user_ans = input("Enter Network ID (e.g., 192.168.x.x): ").strip()
        
        if user_ans == correct_net_id:
            print(f" [✓] CORRECT! Network ID is {correct_net_id}.\n")
            score += 1
        else:
            print(f" [✗] FAILED. Correct Network ID was: {correct_net_id}\n")

    print("-----------------------------------------")
    print(f"DRILL COMPLETE | SCORE: {score}/{rounds}")
    if score == rounds:
        print("STATUS: SUBNETTING REFLEXES OPTIMIZED.")
    else:
        print("STATUS: KEEP DRILLING BLOCK SIZES.")
    print("=========================================")

if __name__ == "__main__":
    run_subnet_drill()