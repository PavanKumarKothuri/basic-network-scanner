
---

# Basic Network Scanner 🔍

A simple yet powerful Python-based tool that scans open ports and identifies potential vulnerabilities on a target machine or network. Perfect for anyone getting started with network security or looking to automate basic network scans! 🚀

---

## Features 🌟

- **Port Scanning**: Quickly checks for open ports in a given range on a target IP. ⚡
- **Target Discovery**: Uses Nmap to perform stealth scans and identify live hosts. 🛠️
- **Detailed Results**: Provides detailed information about each open port and its status. 📊
- **Simple Interface**: Easy-to-use with a single function call. 💡

---

## Requirements 🛠️

Before running the network scanner, make sure you have these installed:

- **Python 3.x** (Preferably 3.6 or later) 🐍
- **Nmap**: This tool leverages Nmap for port scanning. You’ll need to install it separately. 🌐
- **Python Nmap library**: Install via pip:
  
  ```bash
  pip install python-nmap
  ```

---

## Installation 🚀

1. **Install Nmap**:
   - Windows: [Download Nmap for Windows](https://nmap.org/download.html)
   - Linux/macOS: Use your package manager:
     ```bash
     sudo apt install nmap  # Ubuntu/Debian
     brew install nmap      # macOS
     ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/basic-network-scanner.git
   cd basic-network-scanner
   ```

3. **Install dependencies**:
   ```bash
   pip install python-nmap
   ```

---

## Usage 🔧

### **Run the Network Scanner**:

Use the script to scan a specific target IP and port range:

```python
from network_scanner import basic_network_scanner

target_ip = "192.168.1.1"  # Replace with your target IP
port_range = "1-1024"      # Replace with the range of ports you want to scan

basic_network_scanner(target_ip, port_range)
```

The script will output the open ports and their statuses on the target IP. 💻🔓

---

## How It Works 🔍

1. The tool initializes the **Nmap Port Scanner** using Python.
2. A stealth scan (`-sS`) is performed on the specified target IP.
3. The script retrieves results and parses the open TCP ports.
4. It prints out the status of each open port (e.g., open, closed, filtered).

---

## Example Output 💬

```
Starting Nmap scan on target: 192.168.1.1
Port 22 is open (SSH).
Port 80 is open (HTTP).
Port 443 is closed (HTTPS).
```

If no open ports are found:
```
No open TCP ports found on 192.168.1.1.
```

---

## Contributing 🤝

We welcome contributions! 🎉 If you'd like to contribute, feel free to fork the repository, create a new branch, and submit a pull request with your changes.

---

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🚀 Let’s Secure the Network Together!

Happy scanning! 🔍 If you have any issues or questions, feel free to open an issue or ask in the discussions tab. Let’s make the network safer! 🛡️

---
## **📫 Author**
- PavanKumar Kothuri
- 🌐 [LinkedIn Profile](https://www.linkedin.com/in/iamkpk/)
- 💻 [GitHub Profile](https://github.com/PavanKumarKothuri)  
- ✉️ [Email: pavankumarkothuri9@gmail.com](mailto:pavankumarkothuri9@gmail.com)

Let me know if you need any modifications!