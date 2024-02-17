import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
connection.sendto("Hol erem el az adatokat", server_address)
data, address = connection.recvfrom(4096)
print "Cim:", data 
Seederaddress=eval(data)
connection.sendto("Mi az adat", Seederaddress)
Sdata, Saddress = connection.recvfrom(4096)
print "Kosz tes: ",Sdata
connection.close()