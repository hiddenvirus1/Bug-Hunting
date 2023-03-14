import requests
import argparse

def find_subdomains(domain):
    subdomains = []
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        for item in data:
            name_value = item.get('name_value', '')
            if name_value:
                subdomains.append(name_value)
    return subdomains

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find subdomains using crt.sh')
    parser.add_argument('-d', '--domain', type=str, required=True, help='The domain to find subdomains for')
    args = parser.parse_args()
    subdomains = find_subdomains(args.domain)
    for subdomain in subdomains:
        print(subdomain)
