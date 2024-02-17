import socket

for responde in socket.getaddrinfo('www.python.org','http'):
    family, socktype, proto, canonname, shockaddr=responde
    print family, socktype, proto, canonname, shockaddr
