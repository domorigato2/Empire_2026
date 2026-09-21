def calculate_magic_number(cidr):
    masks = {24: 0, 25: 128, 26: 192, 27: 224, 28: 240, 29: 248, 30: 252}
    if cidr not in masks:
        return "Unsupported CIDR."
    octet_val = masks[cidr]
    magic_num = 256 - octet_val
    usable_hosts = (2 ** (32 - cidr)) - 2
    return f"CIDR: /{cidr} | 4th Octet: {octet_val} | Magic Number (Block): {magic_num} | Usable Hosts: {usable_hosts}"

for prefix in range(24, 31):
    print(calculate_magic_number(prefix))
