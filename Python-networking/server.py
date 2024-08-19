import socket
 
# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set socket option to reuse address
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to a specific address and port
s.bind(("127.0.0.1", 6669))

while True:
    Rdata, address = s.recvfrom(1024)
    data = Rdata.decode("utf-8")
    print("Request from {}:\n{}".format(address, data))
    
    # اطلب من المستخدم إدخال رسالة الرد
    msg = input("Enter your response: ")
    
    # ترميز الرسالة وإرسالها إلى العميل
    sdata = msg.encode("utf-8")
    s.sendto(sdata, address)
    
    print("Server Responded...!")
