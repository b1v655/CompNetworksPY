import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
nevjagyzek=[]
server_address = ('localhost', 10000)
sock.bind(server_address)
while True:
    data, address = sock.recvfrom(4096) 
    if data.split('_')[1]=='LOGIN':
        nevjegyzek.append([data.split('_')[2],address]);
    sock.sendto('valami', address)
