import ipaddress

def ipv4_to_binary(ipv4):
    try:
        octets = ipv4.split('.')
        binary_octets = [format(int(octet), '08b') for octet in octets]
        binary_ipv4 = ' '.join(binary_octets)
        return binary_ipv4
    except ValueError:
        return "Invalid IPv4 address."

def ipv6_to_binary(ipv6):
    try:
        ipv6_obj = ipaddress.IPv6Address(ipv6)
        binary_ipv6 = bin(int(ipv6_obj))[2:].zfill(128) 
        binary_ipv6_formatted = ':'.join([binary_ipv6[i:i+16] for i in range(0, len(binary_ipv6), 16)])
        return binary_ipv6_formatted
    except ipaddress.AddressValueError:
        return "Invalid IPv6 address."

def choice():
    version = input("Would you like to translate an IPv4 or IPv6 address? ").strip().lower()

    if version == "ipv4":
        ipv4_address = input("Enter an IPv4 address: ").strip()
        print(f"IPv4 Address: {ipv4_address}")
        print(f"Binary Representation: {ipv4_to_binary(ipv4_address)}")

    elif version == "ipv6":
        ipv6_address = input("Enter an IPv6 address: ").strip()
        print(f"IPv6 Address: {ipv6_address}")
        print(f"Binary Representation: {ipv6_to_binary(ipv6_address)}")

    else:
        print("Invalid choice. Please enter either 'IPv4' or 'IPv6'.")
        choice()

choice()
