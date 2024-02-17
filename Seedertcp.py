import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
connection.connect(server_address)

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Seeker_address = ('localhost', 10001)
sock.bind(Seeker_address)
connection.sendall(str(Seeker_address))

connection.close()

sock.listen(1)

Lconnection, Lclient_address = sock.accept()

Ldata = Lconnection.recv(64)

print "Az kero helye", Lclient_address
print "Az kero uzenete:", Ldata

Lconnection.sendall("zh")