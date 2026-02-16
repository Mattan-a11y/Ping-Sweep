#!/usr/bin/env python3
"""
Network Ping Sweep Tool
Performs network discovery by pinging a range of IP addresses
"""

import subprocess
import ipaddress
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

def ping_host(ip):
    """
    Ping a single IP address and return if it's alive
    
    Args:
        ip: IP address to ping
        
    Returns:
        tuple: (ip, is_alive)
    """
    try:
        # Platform-specific ping command
        param = '-n' if sys.platform.lower() == 'win32' else '-c'
        # Quick ping with 1 second timeout
        command = ['ping', param, '1', '-W', '1', str(ip)]
        
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=2
        )
        
        return (str(ip), result.returncode == 0)
    except Exception:
        return (str(ip), False)

def ping_sweep(network, threads=50):
    """
    Perform ping sweep on a network range
    
    Args:
        network: Network range in CIDR notation (e.g., 192.168.1.0/24)
        threads: Number of concurrent threads
        
    Returns:
        list: List of active IP addresses
    """
    try:
        net = ipaddress.ip_network(network, strict=False)
    except ValueError as e:
        print(f"[ERROR] Invalid network address: {e}")
        return []
    
    print(f"[*] Starting ping sweep on {network}")
    print(f"[*] Scanning {net.num_addresses} addresses...")
    print(f"[*] Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    active_hosts = []
    
    # Use ThreadPoolExecutor for concurrent pinging
    with ThreadPoolExecutor(max_workers=threads) as executor:
        # Submit all ping tasks
        future_to_ip = {executor.submit(ping_host, ip): ip for ip in net.hosts()}
        
        # Process completed tasks
        for future in as_completed(future_to_ip):
            ip, is_alive = future.result()
            if is_alive:
                print(f"[+] {ip} is UP")
                active_hosts.append(ip)
    
    print("-" * 50)
    print(f"[*] Scan complete: {len(active_hosts)} host(s) found")
    print(f"[*] End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    return active_hosts

def main():
    parser = argparse.ArgumentParser(
        description='Network Ping Sweep Tool - Discover active hosts on a network',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 ping_sweep.py 192.168.1.0/24
  python3 ping_sweep.py 10.0.0.0/24 -t 100
  python3 ping_sweep.py 172.16.0.0/16 -o results.txt
        """
    )
    
    parser.add_argument('network', help='Network range in CIDR notation (e.g., 192.168.1.0/24)')
    parser.add_argument('-t', '--threads', type=int, default=50, 
                        help='Number of concurrent threads (default: 50)')
    parser.add_argument('-o', '--output', help='Output file for results')
    
    args = parser.parse_args()
    
    # Perform the ping sweep
    active_hosts = ping_sweep(args.network, args.threads)
    
    # Save results if output file specified
    if args.output and active_hosts:
        with open(args.output, 'w') as f:
            f.write(f"Ping Sweep Results - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Network: {args.network}\n")
            f.write("-" * 50 + "\n")
            for host in active_hosts:
                f.write(f"{host}\n")
        print(f"[*] Results saved to {args.output}")

if __name__ == "__main__":
    main()
