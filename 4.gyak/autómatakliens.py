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
  
  def handleIncomingMessageFromRemoteServer(self,akt):
        data = self.client.recv(3)
        if data=='end' :
          print 'end'
          print '\nDisconnected from server'
          sys.exit()
        if data=='win' :
          print 'win'
          print '\nDisconnected from server'
          sys.exit()
        if data=='yes':
          if akt[0]=='<':
            interval[1]=int(akt.split(' ')[1])-1
 
          if akt[0]=='>':
            interval[0]=int(akt.split(' ')[1])+1
         
        if data=='no':
          if akt[0]=='<':
            interval[0]=int(akt.split(' ')[1])
          
          if akt[0]=='>':
            interval[1]=int(akt.split(' ')[1])
     
        print data
  def handleConnection(self):
    while True:
        if interval[0]-interval[1]==0:
          akt='= '+str(interval[0])
        else:
          akt=random.choice(ops)+" "+str(random.randint(interval[0], interval[1]))
        self.client.send(akt)
        print akt
        self.handleIncomingMessageFromRemoteServer(akt)
        time.sleep(1)

simpleTCPSelectClient = SimpleTCPSelectClient()
simpleTCPSelectClient.handleConnection()
