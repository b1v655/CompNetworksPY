import socket
import sys
import random
import time
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
        data = self.client.recv(11)
        print data
  def handleConnection(self):
        self.client.send("kerem")
        self.handleIncomingMessageFromRemoteServer()

simpleTCPSelectClient = SimpleTCPSelectClient()
simpleTCPSelectClient.handleConnection()
