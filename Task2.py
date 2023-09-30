import re

def validate_ipv4(ip):
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    if re.match(ipv4_pattern, ip):
        octets = ip.split('.')
        
        for octet in octets:
            if not 0 <= int(octet) <= 255:
                return False
        return True
    else:
        return False


ip_address = input("Enter an IPv4 address: ")
if validate_ipv4(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is not a valid IPv4 address.")


print(" ")
print("You have exicuted the code succesfuly")