import socket

# Define the target host and the list of ports to scan
host = input('Enter your target host=> ')
ports = [20, 21, 22, 23, 80, 443]

# Loop through each port in the list
for port in ports:
    # Create a new socket for each port
    connection = socket.socket()
    
    # Set a timeout for the connection attempt (2 seconds)
    connection.settimeout(2)
    
    try:
        # Try to connect to the target host on the current port
        connection.connect((host, port))
        
        # If successful, print that the port is open
        print("Port " + str(port) + " Open")
    
    except:
        continue
    # Close the connection
    connection.close()
