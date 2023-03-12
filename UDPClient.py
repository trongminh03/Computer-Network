import socket

# Define the IP address and port for the server
ip_address = '127.0.0.1'
port = 6000

# Create a UDP socket object
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to the server
while True:
    message = input("Client: ")
    if message == 'quit': break
    udp_socket.sendto(message.encode(), (ip_address, port))

    # Receive a response from the server
    response, server_address = udp_socket.recvfrom(1024)

    # Print the response from the server
    print('Response from server: {}'.format(response.decode()))