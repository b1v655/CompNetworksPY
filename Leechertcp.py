import socket
import struct

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
connection.connect(server_address)

connection.sendall("Kernek adatokat")

data = connection.recv(64)

connection.close()
print "Adat cim", data
Sconnection=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Sconnection.connect(eval(data))

Sconnection.sendall("mivan")

da=Sconnection.recv(64)
print da
Sconnection.close()