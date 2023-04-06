import argparse
import jsonlines

# Parse the command-line arguments
parser = argparse.ArgumentParser(description='Read Shodan results from a JSON file.')
parser.add_argument('-f', '--filename', required=True, help='Path to the input file')
parser.add_argument('-ip', action='store_true', help='Print only the IP addresses')
args = parser.parse_args()

# Open the file and read the JSON data
with open(args.filename, 'r') as f:
    results = jsonlines.Reader(f)

    # Loop through each result in the JSON data
    for result in results:
        # Extract the IP address from the result
        ip_address = result['ip_str']

        # Print only the IP address if specified by the user
        if args.ip:
            print(ip_address)
        else:
            # Extract the other fields if not printing only the IP addresses
            hostnames = result.get('hostnames', [])
            domains = result.get('domains', [])
            open_ports = result.get('port', [])
            if not isinstance(open_ports, list):
                open_ports = [open_ports]  # Convert to a list if not already a list
            status = result.get('http', {}).get('status', '') or result.get('https', {}).get('status', '')
            org_name = result.get('org', '')
            
            # Print the data to the console
            print(f"IP Address: {ip_address}")
            if hostnames:
                print(f"Hostnames: {', '.join(hostnames)}")
            if domains:
                print(f"Domains: {', '.join(domains)}")
            if open_ports:
                print(f"Open ports: {', '.join(map(str, open_ports))}")
            if status:
                print(f"Status: {status}")
            if org_name:
                print(f"Organization: {org_name}")

            # Print a separator line between each result
            print("=====================================")
