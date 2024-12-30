# Importing required libraries
import nmap  # Python-nmap library for port scanning

def basic_network_scanner(target_ip, port_range):
    """
    A simple network scanner to detect open ports on a target IP.

    Parameters:
    - target_ip (str): The IP address to scan.
    - port_range (str): The range of ports to scan (e.g., "20-1000").

    Returns:
    - None
    """
    # Create an instance of the PortScanner class
    scanner = nmap.PortScanner()

    print(f"Scanning target: {target_ip} on ports: {port_range}")

    try:
        # Perform the scan
        scan_result = scanner.scan(hosts=target_ip, ports=port_range, arguments='-sS -v')

        # Check if the target is up
        if 'up' in scan_result['scan'][target_ip]['status']['state']:
            print(f"Target {target_ip} is up.\n")
        else:
            print(f"Target {target_ip} appears to be down.\n")
            return

        # Retrieve scan results
        for port in scanner[target_ip]['tcp']:
            port_info = scanner[target_ip]['tcp'][port]
            state = port_info['state']
            service = port_info['name']
            print(f"Port {port} is {state} (Service: {service})")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    print("Welcome to the Basic Network Scanner!")
    target = input("Enter the target IP address (e.g., 192.168.1.1): ").strip()
    port_range = input("Enter the port range to scan (e.g., 20-1000): ").strip()

    basic_network_scanner(target, port_range)
