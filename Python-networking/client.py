import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to the server
while True:
    msg = str(input("Enter your message: "))
    sdata = msg.encode("utf-8")
    
    # إرسال البيانات إلى عنوان الخادم ومنفذه
    sock.sendto(sdata, ("127.0.0.1", 6669))
    
    # استقبال الرد من الخادم
    Rdata, address = sock.recvfrom(1024)
    data = Rdata.decode("utf-8")  # تغيير Rdata إلى data بعد فك التشفير
    print("Response from server: {}".format(data))