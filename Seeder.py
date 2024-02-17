import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
connection.sendto("Seeder kesz", server_address)

ldata, laddress = connection.recvfrom(4096)
print "Az leecher helye", laddress
print "Az leacher uzenete:", ldata
connection.sendto("ZH", laddress)
connection.close()