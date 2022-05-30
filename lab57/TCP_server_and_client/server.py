import socket
import threading


PORT = 5050
SERVER_IP = '127.0.0.1'
ENCODING='utf-8'
BUFSIZE=1024

# SERVER_IP = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind server to socket and start listening
server.bind((SERVER_IP,PORT))
server.listen()

print(f'Server is listening on ({SERVER_IP},{PORT})...')


clients=list()

def broadcast(message,client_to_exclude):
	for client in clients:
		if client != client_to_exclude:
			print(f'Send message "{message}" to {client.getpeername()}')
			client.send(message.encode(ENCODING))


def handle_client(client):
	while True:
		try:
			msg=client.recv(BUFSIZE).decode(ENCODING)
			if msg:
				print(f'Received from {client.getpeername()}: {msg}')
				broadcast(msg,client)
			else:
				client.close()
		except Exception as err:
			print(f'ERROR: {err}')
			clients.remove(client)
			client.close()
			break


while True:
	(client, port)=server.accept()
	print(f'Client is connected {port}')

	clients.append(client)
	print(f'clients len: {len(clients)}')

	tr = threading.Thread(target=handle_client,args=(client,))
	tr.start()









