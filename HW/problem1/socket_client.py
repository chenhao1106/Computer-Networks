# -*- coding: utf-8 -*-
import socket

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.connect( ( "127.0.0.1", 6066 ) )
print( "connect to " + "127.0.0.1" )

while( True ):
    print( "Receive server message: " )
    print( s.recv( 1024 ).decode( "utf-8" ), end ='' ) 
    
    question = input()
    s.send( question.encode( "utf-8" ) )
    
    print( "Receive server message: " )
    print( s.recv( 1024 ).decode( "utf-8" ) )
    print( s.recv( 1024 ).decode( "utf-8" ) )
    
    reply = input()
    s.send( reply.upper().encode( "utf-8" ) )
    
    if reply.upper() == 'N':
        break

s.close()