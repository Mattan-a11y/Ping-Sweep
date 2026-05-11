# network-ping-sweep

A multithreaded ping sweep tool for quick host discovery across a network range. Written in pure Python — no external dependencies.

## Features

- CIDR notation support (`/24`, `/28`, etc.)
- Multithreaded scanning with adjustable thread count
- Optional results export to file
- Works on Windows, Linux, and macOS

## Requirements

Python 3.6+, nothing else.

## Installation

```bash
git clone https://github.com/Mattan-a11y/network-ping-sweep.git
cd network-ping-sweep

# Linux/macOS
chmod +x ping_sweep.py
```

## Usage

```bash
# Basic scan
python3 ping_sweep.py 192.168.1.0/24

# More threads
python3 ping_sweep.py 192.168.1.0/24 -t 100

# Save output
python3 ping_sweep.py 192.168.1.0/24 -o results.txt

# Combined
python3 ping_sweep.py 10.0.0.0/24 -t 75 -o scan_results.txt
```

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `network` | Target range in CIDR notation | Required |
| `-t, --threads` | Concurrent threads | 50 |
| `-o, --output` | Save results to file | — |

## Example output

```
[*] Starting ping sweep on 192.168.1.0/24
[*] Scanning 254 addresses...
[*] Start time: 2024-02-16 14:30:00
--------------------------------------------------
[+] 192.168.1.1 is UP
[+] 192.168.1.10 is UP
[+] 192.168.1.100 is UP
--------------------------------------------------
[*] Scan complete: 3 host(s) found
[*] End time: 2024-02-16 14:30:15
```

## Notes

- Only use this on networks you own or have explicit permission to scan
- ICMP may be blocked depending on firewall rules
- Large ranges (`/16` and up) will take considerably longer

## License

MIT

## Author

[@Mattan-a11y](https://github.com/Mattan-a11y) · [LinkedIn](https://www.linkedin.com/in/matin-shahid-1b426a217/)
