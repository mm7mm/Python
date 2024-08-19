
import socket


# Get IP address of a given domain name
ip = socket.gethostbyname("google.com")
print(ip)


# Get domain name of a given IP address
host = socket.gethostbyaddr(str(ip))
print(host)


# Get service name of a given port number (in this case, http port 80)
port = socket.getservbyname("http")
print(port)


# Get service name of a given port number (in this case, ftp port 21)
service_name = socket.getservbyport(21)
print(service_name)
