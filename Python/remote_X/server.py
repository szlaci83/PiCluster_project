#!/usr/bin/python
from thread import *
from socket import *

HOST = '10.42.0.1.'
PORT = 4567

def clientthread(conn):
     print('Client connected on: ' + conn.getpeername()[0])	
     while True:
	 command = raw_input('PI>')
         command = str(command)
         print(command)
	 conn.send(command)
         if command=='exit':
		print('exiting')
		break  
         data = conn.recv(1024)
         print(data)

sock = socket()
sock.bind((HOST, PORT))
sock.listen(8)  
print('Server started, waiting for connection on port : ' + str(PORT))

while True:
    conn, addr = sock.accept()
    start_new_thread(clientthread,(conn,))

conn.close()
sock.close()
