import socket
import sys
import random
import time
class SimpleTCPSelectClient:
  def __init__(self, serverAddr='localhost', serverPort=9999):
    self.setupClient(serverAddr, serverPort)

  def setupClient(self, serverAddr, serverPort):
    server_address = (serverAddr, serverPort)

    # Create a TCP/IP socket
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the port where the server is listening
    self.client.connect(server_address)
  
  def handleIncomingMessageFromRemoteServer(self):
        data, address = connection.recvfrom(4096)
        print data 
        manoaddress=eval(data)
        connection.sendto("barmi", manoaddress)
        Sdata, Saddress = connection.recvfrom(4096)
        print Sdata
        connection.close()
  def handleConnection(self):
        self.client.send("9999")
        self.handleIncomingMessageFromRemoteServer()

simpleTCPSelectClient = SimpleTCPSelectClient()
simpleTCPSelectClient.handleConnection()
