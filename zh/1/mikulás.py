import socket
import sys
server = socket.socket()

server_address = ('localhost',10003)
server.bind(server_address)
server.listen(1)
client,client_address=server.accept()
data=client.recv(16)
ajandek={'Gabor':'valamit','Peti':'semmit'}
print data
cucc=""
if data in ajandek:
    cucc=ajandek[data]
    del ajandek[data]
else:
    cucc="virgacs"
client.sendall(cucc)
print ajandek
sys.exit()
