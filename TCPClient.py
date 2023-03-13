import socket

# create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to a server
server_address = ('localhost', 8000)
client_socket.connect(server_address)

# send a message to the server
while True:
    message = input('Client: ') 
    if message == 'quit': break 
    client_socket.send(message.encode())

    # receive a response from the server
    response = client_socket.recv(1024)
    print(f'Response from server: {response.decode()}')
    
# close the socket
client_socket.close()