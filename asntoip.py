import requests
import datetime
import subprocess

def fetch_asn_data(asn):
    url = f"https://ipinfo.io/widget/demo/{asn}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching ASN data: {e}")
        return None

def extract_ip_range(ip, range_end="1-254"):
    ip_parts = ip.split('.')
    if len(ip_parts) == 4:
        ip_parts[-1] = range_end
        return '.'.join(ip_parts)
    return ip

def extract_netblocks(data):
    netblocks = []
    prefixes = data.get("prefixes", [])
    for prefix in prefixes:
        netblock = prefix.get("netblock")
        if netblock:
            ip = netblock.split('/')[0]  # Extract only the IP part
            ip_range = extract_ip_range(ip)
            netblocks.append(ip_range)
    return netblocks

def save_netblocks_to_file(netblocks, name):
    name = name.replace(" ", "_")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.txt"
    with open(filename, "w") as file:
        for netblock in netblocks:
            file.write(netblock + "\n")
    return filename

def scan_ip_range(ip_range):
    try:
        result = subprocess.run(['nmap', '-sn', ip_range], capture_output=True, text=True)
        output = result.stdout
        responding_ips = []
        for line in output.split('\n'):
            if "Nmap scan report for" in line:
                ip = line.split()[-1].strip('()')  # Remove parentheses from IP
                responding_ips.append(ip)
        return responding_ips
    except FileNotFoundError:
        print("Error: 'nmap' not found. Please ensure it is installed.")
        return []

def save_responding_ips_to_file(responding_ips, name):
    name = name.replace(" ", "_")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}_responded.txt"
    with open(filename, "w") as file:
        for ip in responding_ips:
            file.write(ip + "\n")
    return filename

def main():
    asn = input("Please enter your ASN (e.g., AS12345): ")
    if not asn.startswith("AS") or not asn[2:].isdigit():
        print("Invalid ASN format. Please enter a valid ASN starting with 'AS' and followed by digits.")
        return

    data = fetch_asn_data(asn)
    if data:
        netblocks = extract_netblocks(data)
        if netblocks:
            name = data.get("name", "default_name").replace(" ", "_")
            netblocks_filename = save_netblocks_to_file(netblocks, name)
            print(f"Netblocks have been saved to {netblocks_filename}.")
            
            responding_ips = []
            for netblock in netblocks:
                responding_ips.extend(scan_ip_range(netblock))
            
            if responding_ips:
                responding_ips_filename = save_responding_ips_to_file(responding_ips, name)
                print(f"Responding IPs have been saved to {responding_ips_filename}.")
            else:
                print("No responding IPs found in the scanned ranges.")
        else:
            print("No netblocks found in the ASN data.")
    else:
        print("Failed to fetch data. Please check the ASN and try again.")

if __name__ == "__main__":
    main()
