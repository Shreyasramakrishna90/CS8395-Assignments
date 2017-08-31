#Server program Shreyas Ramakrishna

import zmq
import time

#creating context inorder to create socket
context = zmq.Context()

#Define the socket and bind it
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#Run the message send and receive part
#print("waiting for a client to connect")
while True:
	print("waiting for a client to connect")
        message = socket.recv()
        time.sleep(1)
        socket.send( message)
        print(message)

