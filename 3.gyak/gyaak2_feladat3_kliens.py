import socket
client = socket.socket()

server_addr = ('localhost',10000)
client.connect(server_addr)
for i in range (20): 
    client.sendall('Hello client')

    data=client.recv(16)

    print data
client.close()
