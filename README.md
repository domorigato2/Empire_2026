# Dominic Empire OS v2.4

An opinionated, terminal-first operations and network telemetry suite built in Python and Windows PowerShell.

## Core Modules

- **`empire.py`**: Central CLI orchestrator managing sub-process execution and persistent vault storage.
- **`net_probe.py`**: Automated CCNA reachability diagnostic verifying Layer 2/3 Default Gateway routing, Layer 3 ISP Backbone connectivity, and Layer 7 DNS resolution.
- **`subnet_calc.py`**: High-performance CCNA IPv4 subnet calculator computing Network ID, Broadcast ID, CIDR masks, total addresses, and usable host ranges in O(1) time complexity.
- **`port_scanner.py`**: Native Layer 4 TCP socket scanner probing standard CCNA service ports (DNS, HTTP, HTTPS, SSH) via 3-way handshake.
- **`ccna_quiz.py`**: Interactive terminal drill engine testing core CCNA 200-301 routing protocols, subnetting, and administrative distances.
- **`streaks.py`**: Operational streak vault monitoring chemical sobriety, physical uptime, and habit automation.
- **`empire_log.py`**: Real-time biological telemetry tracker with conditional logic gates calculating daily allocations and nicotine abstinence streaks.
- **`war_chest.py`**: Financial projection engine tracking emergency capital growth toward a $1,000 baseline with terminal progress visualization.

## Technical Stack

- **Language**: Python 3.12
- **Environment**: Windows PowerShell / Git Version Control
- **Architecture**: Modular CLI / Subprocess Automation