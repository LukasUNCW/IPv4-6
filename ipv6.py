import ipaddress
# Function to convert IPv6 address to binary

def ipv6_to_binary(ipv6):
    # Convert IPv6 address to a 128-bit integer
    ipv6_obj = ipaddress.IPv6Address(ipv6)
    binary_ipv6 = bin(int(ipv6_obj))[2:].zfill(128) # Convert to binary and ensure it's 128 bits long

    # Format the binary IPv6 in groups of 16 bits for readability
    binary_ipv6_formatted = ':'.join([binary_ipv6[i:i+16] for i in range(0, len(binary_ipv6), 16)])
    
    return binary_ipv6_formatted

# Get IPv6 address input from the user
ipv6_address = input("Enter an IPv6 address: ")

# Convert the input IPv6 address to binary
binary_representation = ipv6_to_binary(ipv6_address)

# Display the result
print (f"IPv6 Address: {ipv6_address}")
print(f"Binary Representation: {binary_representation}")
