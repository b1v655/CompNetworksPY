import socket
import sys
client = socket.socket()

server_addr = ('localhost',10003)
client.connect(server_addr)
client.sendall(sys.argv[1])
data=client.recv(16)

print data
client.close()
