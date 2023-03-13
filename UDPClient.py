import socket

# Define the IP address and port for the server
ip_address = '127.0.0.1'
port = 6000

# Create a UDP socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to the server
while True:
    message = input("Client: ")
    if message == 'quit': break
    # convert msg from string type to byte type and send it to the server
    client_socket.sendto(message.encode(), (ip_address, port))

    # Receive a response from the server
    response, server_address = client_socket.recvfrom(2048)
    #'2048' parameter is buffer size, specifies the maximum number of bytes to be received in a single call

    # Print the response from the server
    print('Response from server: {}'.format(response.decode()))

client_socket.close()