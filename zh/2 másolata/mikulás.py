
import select
import socket
import sys
import random


class SimpleTCPSelectServer:
  
  def __init__(self, addr='localhost', port=9999, timeout=1):
    self.server = self.setupServer(addr, port)
    # Sockets from which we expect to read
    self.inputs = [ self.server ]
    # Wait for at least one of the sockets to be ready for processing
    self.timeout=timeout

  def setupServer(self, addr, port):
    # Create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to the port
    server_address = (addr, port)
    server.bind(server_address)
    
    # Listen for incoming connections
    server.listen(5)
    return server

  def handleNewConnection(self, sock):
    # A "readable" server socket is ready to accept a connection
    connection, client_address = sock.accept()
    connection.setblocking(0)	# or connection.settimeout(1.0)    
    self.inputs.append(connection)

  def handleDataFromClient(self, sock):
        data = sock.recv(10)
        if data%2==0:
          mano1adress=('localhost', 10004)
          sock.sendall(mano1adress)
        else:
          mano2adress=('localhost', 10005)
          sock.sendall(mano2adress)
        self.inputs.remove(sock)
        sock.close()
  def handleInputs(self, readable):
    for sock in readable:
        if sock is self.server:
            self.handleNewConnection(sock)
        else:
            self.handleDataFromClient(sock)

  def handleExceptionalCondition(self, exceptional):
    for sock in exceptional:
      print >>sys.stderr, 'handling exceptional condition for', sock.getpeername()
      # Stop listening for input on the connection
      self.inputs.remove(sock)
      sock.close()

  def handleConnections(self):
    while self.inputs:
      try:
        readable, writable, exceptional = select.select(self.inputs, [], self.inputs, self.timeout)
    
        if not (readable or writable or exceptional):
            #print >>sys.stderr, '  timed out, do some other work here'
            continue
    
        self.handleInputs(readable)
        self.handleExceptionalCondition(exceptional)
      except KeyboardInterrupt:
        print "Close the system"
        for c in self.inputs:
            c.close()
        self.inputs = []

simpleTCPSelectServer = SimpleTCPSelectServer()
simpleTCPSelectServer.handleConnections()
