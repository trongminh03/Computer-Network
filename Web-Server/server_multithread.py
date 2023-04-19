#import socket module
from socket import *
import threading
import sys # In order to terminate the program

def serve_client(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024).decode()
        print(message)
        filename = message.split()[1] 
        f = open(filename[1:]) 
        outputdata = f.read()
        
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())
        
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        
    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverPort = 6789
serverSocket.bind(('192.168.134.11', serverPort))
serverSocket.listen(5)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print(f'Connected by {addr}')
    
    # Create a new thread to handle the client request
    t = threading.Thread(target=serve_client, args=(connectionSocket, addr))
    t.start()
    
serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data