import sys
import re

def parse_server_log(log_filepath):
    print("\n==================================================")
    print("      NOC AUTOMATION // SERVER LOG PARSER         ")
    print("==================================================")
    print(f" Target File : {log_filepath}")
    print(" Parsing log stream for security and error metrics...")
    print("--------------------------------------------------")

    try:
        with open(log_filepath, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"[!] Error: File '{log_filepath}' not found.")
        return

    total_requests = len(lines)
    errors_404 = 0
    server_errors_500 = 0
    failed_logins = 0
    ip_addresses = {}

    for line in lines:
        # Extract IP addresses (IPv4 pattern)
        ip_match = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)
        if ip_match:
            ip = ip_match.group(1)
            ip_addresses[ip] = ip_addresses.get(ip, 0) + 1

        # Track HTTP status codes
        if " 404 " in line:
            errors_404 += 1
        elif " 500 " in line or " 502 " in line:
            server_errors_500 += 1

        # Track failed SSH/auth logins
        if "Failed password" in line or "Invalid user" in line:
            failed_logins += 1

    print(f" Total Log Lines Processed : {total_requests}")
    print(f" HTTP 404 (Not Found)      : {errors_404}")
    print(f" HTTP 5xx (Server Faults)  : {server_errors_500}")
    print(f" Failed Auth / Brute-Force : {failed_logins}")
    print("--------------------------------------------------")
    print(" Top Active Source IPs:")
    sorted_ips = sorted(ip_addresses.items(), key=lambda x: x[1], reverse=True)
    for ip, count in sorted_ips[:3]:
        print(f"    --> {ip} ({count} requests)")
    print("==================================================\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse_server_log(sys.argv[1])
    else:
        print("[!] Usage: python log_parser.py <LOG_FILE_PATH>")
