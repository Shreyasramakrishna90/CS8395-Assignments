#Client program Shreyas Ramakrishna

import zmq
import sys
import time

#Define a context to create socket
context = zmq.Context()

#use the context to create socket and connect
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#send a message using the socket
print("sending message to server")
time.sleep(1)
print("Hello from ZMQ")
socket.send("Hello from ZMQ")
time.sleep(2)
print("message received from server")
reply= socket.recv()
for x in range (2):
	print(reply)

