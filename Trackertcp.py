import socket
import struct
import operator

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
sock.bind(server_address)

sock.listen(2)

Sconnection, Sclient_address = sock.accept()


Sdata = Sconnection.recv(64)

print "Az adat helye", Sclient_address
print "Az adat uzenete:", Sdata

Lconnection, Lclient_address = sock.accept()

Ldata = Lconnection.recv(64)

print "Az Leecher helye", Lclient_address
print "Az Leechr uzenete:", Ldata

Lconnection.sendall(str(Sdata))