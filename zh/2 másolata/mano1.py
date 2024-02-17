import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10004)
sock.bind(server_address)

data, address = sock.recvfrom(4096)
x=random.randint(0,10)
if x<4:
    sock.sendto("Virgacs", Laddress)
elif x<7:
    sock.sendto("Szaloncukor", Laddress)
else:
    sock.sendto("labda", Laddress)

