from pydoc import cli
import socket

PORT = 5050
SERVER_IP = '127.0.0.1'
ENCODING='utf-8'
BUFSIZE=1024

# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect client to the server:
client.connect((SERVER_IP, PORT))

def recieve_messages():
	msg = client.recv(BUFSIZE).decode(ENCODING)
	print(msg)

while True:
	# send message to server:
	msg = input('MSG:')
	client.send(msg.encode(ENCODING))

	recieve_messages()


client.close()


