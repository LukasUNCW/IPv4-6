def ipv4_to_binary(ipv4):
# Split the IPv4 address into its four octets
    octets = ipv4.split('.')
    # Convert each octet to binary and ensure it's 8 bits long (pad with zeros if necessary)
    binary_octets = [format (int(octet), '08b') for octet in octets]
    # Join the binary octets with a dot for readability
    binary_ipv4 = ' '.join (binary_octets)

    return binary_ipv4

# Get IPv4 address input from the user
ipv4_address = input("Enter an IPv4 address: ")

# Convert the input IPv4 address to binary
binary_representation = ipv4_to_binary(ipv4_address)

# Display the result
print(f"IPv4 Address: {ipv4_address}")
print(f"Binary Representation: {binary_representation}")