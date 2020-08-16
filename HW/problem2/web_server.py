#import socket module
from socket import *
import time
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket

HOST, PORT = "YOUR IP ADDRESS", 8080

serverSocket.bind( ( HOST, PORT ) )
serverSocket.listen( 0 )

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, address = serverSocket.accept()
    try:
        # Receive http request from the clinet
        message = connectionSocket.recv( 1024 ).decode( "utf-8" )
        print( message )

        filename = message.split()[1]
        filename = filename.lstrip('/')
        print( filename )

        f = open( filename, "r" ) 
        # Read data from the file that the client requested
        # Split the data into lines for future transmission 
        outputdata = []
        for line in f:
            outputdata.append( line )
        print(outputdata)

        #Send one HTTP header line into socket
        proto = "HTTP/1.1"
        connectionSocket.send( proto.encode( "utf-8" ) ) 
        # send HTTP status to client
        status = "200 OK\n"
        connectionSocket.send( status.encode( "utf-8" ) )
        # send content type to client
        content = "Content-Tyoe: text/html: charset=UTF-8\n\n"
        connectionSocket.send( content.encode( "utf-8" ) )
        
        # Send the content of the requested file to the client  
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
        
    except IOError:
        #Send response message for file not found
        header = "HTTP/1.1 404 Not Found\n\n"
        connectionSocket.send( header.encode( "utf-8" ) )

        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
