# ASN TO IP RANGE + IP List + Scan Tool

This script fetches IP ranges associated with a given Autonomous System Number (ASN) and scans them for responding hosts. It outputs the results into timestamped files for further analysis.

## Features
- Fetches IP ranges (netblocks) using an ASN lookup.
- Scans the fetched IP ranges using Nmap.
- Saves both the netblocks and responding IPs into timestamped text files.
- Handles errors such as invalid ASN input, missing Nmap, or network issues gracefully.

---

## Requirements

1. **Python Version**: Python 3.7 or higher
2. **Dependencies**:
    - `requests` library for HTTP requests
    - `python-nmap` (optional) for improved scanning (replace `subprocess` if needed)

### Installation
Run the following command to install dependencies:

```bash
pip install -r requirements.txt
```

### Requirements File:
```
requests==2.31.0
python-nmap==0.7.1
```

---

## Prerequisites

### Nmap Installation
The script uses **Nmap** to perform network scans. If Nmap is not installed, download and install it from:

[Download Nmap](https://nmap.org/dist/nmap-7.95-setup.exe)

Ensure that the `nmap` command is available in your system's PATH.

### Verify Nmap Installation:
```bash
nmap --version
```

---

## Usage

### 1. Run the Script
```bash
python asntoip.py
```

### 2. Enter ASN
Input an ASN in the format `AS12345` when prompted.

Example:
```
Please enter your ASN (e.g., AS12345): AS137967
```

### 3. Output
- **Netblocks File**: Saved as `ASNName_YYYYMMDD_HHMMSS.txt`
- **Responding IPs File**: Saved as `ASNName_YYYYMMDD_HHMMSS_responded.txt`

Both files are created in the current directory.

---

## Error Handling
1. **Invalid ASN Format**:
   - The script checks for valid ASN input (e.g., `AS12345`).
   - Invalid formats display an error message.

2. **No Data from API**:
   - Prints an error if the API does not return data for the given ASN.

3. **Nmap Not Installed**:
   - Displays a message indicating that Nmap is missing.
   - Provides the download link for manual installation.

4. **Network Errors**:
   - Handles HTTP and connection errors with appropriate messages.

---

## Example Output
### Netblocks File:
```
192.168.1.0/24
192.192.2.0/24
```

### Responding IPs File:
```
192.168.1.1
192.168.1.2
192.168.1.3
```

---

## Troubleshooting
- If the script cannot find Nmap, verify that it is installed and available in the PATH.
- Double-check the ASN format (must start with `AS` followed by numbers).
- Ensure internet connectivity for fetching ASN data.

---

## License
This project is licensed under the MIT License.

---

## Contributions
Contributions are welcome! Feel free to fork this repository and submit pull requests.

