import socket
import threading

PORT = 5050
SERVER_IP = '127.0.0.1'
ENCODING='utf-8'
BUFSIZE=1024

# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect client to the server:
client.connect((SERVER_IP, PORT))

def recieve_messages(client):
	while True:
		try:
			msg = client.recv(BUFSIZE).decode(ENCODING)
			print(f'>{msg}')
		except Exception as err:
			print(f'ERROR: {err}')
			client.close()
			break

tr = threading.Thread(target=recieve_messages,args=(client,))
tr.start()

while True:
	# send message to server:
	msg = input(f'<:')
	if msg:
		client.send(msg.encode(ENCODING))




