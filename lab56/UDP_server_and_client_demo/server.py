import socket
import threading

HOST = '127.0.0.1'
PORT = 9000
BUFSIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# asociate server with (HOST,PORT)
server.bind((HOST,PORT))

def handle_client():
	# receive message from a client
	msg,address = server.recvfrom(BUFSIZE)
	print(f'MSG Received from: {address}')
	print(msg.decode('utf-8'))

	# send hello to client:
	msg_to_send = 'Hello from server'
	server.sendto(msg_to_send.encode('utf-8'),address)

for i in range(0,5):
	tr = threading.Thread(handle_client())
	tr.start()


