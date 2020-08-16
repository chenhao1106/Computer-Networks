import socket

# Specify the IP addr and port number 
# (use "127.0.0.1" for localhost on local machine)
# Create a socket and bind the socket to the addr
HOST, PORT = "127.0.0.1", 6066 

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.bind( ( HOST, PORT ) )

while(True):
    # Listen for any request
    s.listen( 0 )
    print("The Grading server for HW2 is running..")

    while(True):
        # Accept a new request and admit the connection
        client, address = s.accept()
        print(str(address)+" connected")
        try:
            while (True):
                client.send(b"Welcome to the calculator server. Input your problem ?\n")
                # Recieve the data from the client and send the answer back to the client
                # Ask if the client want to terminate the process
                # Terminate the process or continue

                equation = client.recv( 1024 ).decode( "utf-8" )
                answer = eval( equation )
                reply = "The answer is " + str( answer ) + "."
                
                client.send( reply.encode( "utf-8" ) )
                client.send( b"Do you have any question? (Y/N)" )
               
                if client.recv( 1024 ).upper().decode( "utf-8" ) == "N" :
                    print( str(address) + " disconnected" )
                    client.close()
                    break

        except ValueError:
            print("except")
    