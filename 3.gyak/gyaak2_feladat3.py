import socket
server = socket.socket()

server_address = ('localhost',10000)
server.bind(server_address)
server.listen(1)
client,client_address=server.accept()
for i in range (20):
    

    
    data=client.recv(16)

    print data
    client.sendall('Hello client')
