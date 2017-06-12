#!/usr/bin/python

import subprocess
import socket
import sys

#details of the server
PORT = '4567'
IP = '10.42.0.1'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (IP, PORT)
sock.connect(server_address)
print('Connected, waiting for commands on port:' + PORT)

try:
    sock.listen()
    while True:
	command = sock.recv(1024)
        print(command)
finally:
    print('closing socket')
    sock.close()





def do(args):
	p = subprocess.Popen(args.split(), stdout=subprocess.PIPE)
	output, err = p.communicate()
	print(output)
	return output

if __name__=='__main__':
	do("ping -c 10 www.cyberciti.biz")
