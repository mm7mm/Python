import socket

# Create a TCP/IP socket
s = socket.socket()

# Define the host (localhost) and port
host = '127.0.0.1'
port = 6666

# Bind the socket to the host and port
s.bind((host, port))

# Listen for incoming connections (with a maximum backlog of 1 connection)
s.listen()

# Wait for a connection
print('Waiting for connection')

# Accept a connection from a client
client, addr = s.accept()  # client socket and client address
print('Connected by', addr)

# Close the client connection
client.close()