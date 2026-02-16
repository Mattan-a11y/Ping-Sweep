# Network Ping Sweep Tool

A fast and efficient network discovery tool that performs ping sweeps to identify active hosts on a network.

## 🎯 Features

- **Fast scanning** with multi-threaded execution
- **CIDR notation support** for flexible network ranges
- **Cross-platform** compatibility (Windows, Linux, macOS)
- **Export results** to text file
- **Real-time feedback** showing discovered hosts

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/network-ping-sweep.git
cd network-ping-sweep

# Make the script executable (Linux/macOS)
chmod +x ping_sweep.py
```

## 💻 Usage

### Basic Usage

```bash
# Scan a /24 network
python3 ping_sweep.py 192.168.1.0/24

# Scan a smaller subnet
python3 ping_sweep.py 10.0.0.0/28
```

### Advanced Options

```bash
# Use more threads for faster scanning
python3 ping_sweep.py 192.168.1.0/24 -t 100

# Save results to a file
python3 ping_sweep.py 192.168.1.0/24 -o results.txt

# Combine options
python3 ping_sweep.py 10.0.0.0/24 -t 75 -o scan_results.txt
```

## 📊 Example Output

```
[*] Starting ping sweep on 192.168.1.0/24
[*] Scanning 254 addresses...
[*] Start time: 2024-02-16 14:30:00
--------------------------------------------------
[+] 192.168.1.1 is UP
[+] 192.168.1.10 is UP
[+] 192.168.1.15 is UP
[+] 192.168.1.100 is UP
--------------------------------------------------
[*] Scan complete: 4 host(s) found
[*] End time: 2024-02-16 14:30:15
```

## 🔧 Options

| Option | Description | Default |
|--------|-------------|---------|
| `network` | Network range in CIDR notation | Required |
| `-t, --threads` | Number of concurrent threads | 50 |
| `-o, --output` | Output file for results | None |

## ⚠️ Important Notes

- **Network permissions**: Make sure you have authorization to scan the target network
- **Firewall rules**: ICMP may be blocked on some networks
- **Performance**: Adjust thread count based on your system capabilities
- **Large networks**: Scanning /16 or larger networks may take considerable time

## 🎓 Use Cases

- Network inventory and documentation
- Troubleshooting connectivity issues
- Security audits (with proper authorization)
- Network mapping before deeper scans

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👤 Author

Your Name
- GitHub: [@Mattan-a11y](https://github.com/Mattan-a11y)
- LinkedIn: [Matin Shahid](https://www.linkedin.com/in/matin-shahid-1b426a217/)

## ⚖️ Legal Disclaimer

This tool is for educational and authorized testing purposes only. Always obtain proper authorization before scanning any network you don't own or have explicit permission to test.
