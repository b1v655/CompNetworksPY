import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
sock.bind(server_address)

data, address = sock.recvfrom(4096)

print "Az adat helye", address
print "Az adat uzenete:", data

Ldata, Laddress = sock.recvfrom(4096)

print "Az Leccher helye", Laddress
print "Az Leecher uzenete:", Ldata

sock.sendto(str(address), Laddress)
