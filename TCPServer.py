import socket

# create a TCP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_address = ('localhost', 8000)
server_socket.bind(server_address)

# listen for incoming connections
server_socket.listen(1) 
# '1' is the parameter specifies the maximum number of queued connections (at least 1)
print('Server is listening for incoming connections...')

# accept a client connection
client_socket, client_address = server_socket.accept()
print(f'Client connected: {client_address}')

while True:
    # receive a message from the client
    message = client_socket.recv(1024)
    print(f'Message from client: {message.decode()}')

    # send a response to the client
    # response = 'Hello, client!' 
    response = message.decode().upper()
    client_socket.send(response.encode())
    
    # close the client socket
    # client_socket.close()
