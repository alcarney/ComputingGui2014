#!/usr/bin/python

import socket
import struct

HOST = '127.0.0.1'
PORT = 3490

# Create a new socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
s.connect((HOST,PORT))

# Identify ourselves as the user interface
s.sendall(struct.pack('i', 1))
data = s.recv(4)

# Tell the server how many locations we will send
s.sendall(struct.pack('i', 9))

# Transmit data
for i in range (0,10):

    s.sendall(struct.pack('ddd', i+1, 2*i, 3*i))

    # Wait for acknowledgement before sending next piece of data - I still don't like this though
    data = s.recv(8)
    #print 'Recieved', repr (data)


# Send EOS packet
s.sendall(struct.pack('ddd', 0, 0, 0))

# Close the socket
s.close()
