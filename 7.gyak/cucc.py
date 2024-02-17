import socket
import struct

sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

multicast_group='224.3.29.71'
address=('',10000)
sock.bind(address)

group=socket.inet_aton(multicast_group)

mreq=struct.pack('4sL',group,socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)

print('writeing')
data,sender=sock.recvfrom(4096)
print('incom mess from', multicast_group)
print('mess',data)



sock.sendto('ACK',sender_address)
sock.close
