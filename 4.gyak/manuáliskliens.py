import socket
import sys
import random
import time
ops=['<','>']
interval=[0,100]
class SimpleTCPSelectClient:
  def __init__(self, serverAddr='localhost', serverPort=10003):
    self.setupClient(serverAddr, serverPort)

  def setupClient(self, serverAddr, serverPort):
    server_address = (serverAddr, serverPort)

    # Create a TCP/IP socket
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the port where the server is listening
    self.client.connect(server_address)
  
  def handleIncomingMessageFromRemoteServer(self):
        data = self.client.recv(3)
        if data=='end' :
          print 'end'
          print '\nDisconnected from server'
          sys.exit()
        if data=='win' :
          print 'win'
          print '\nDisconnected from server'
          sys.exit()
        print data
  def handleConnection(self):
    while True:
        
        self.client.send(raw_input())
        self.handleIncomingMessageFromRemoteServer()
        time.sleep(1)

simpleTCPSelectClient = SimpleTCPSelectClient()
simpleTCPSelectClient.handleConnection()
