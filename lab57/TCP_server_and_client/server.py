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
			print(f'Send meg to {client.raddr}')
			client.send(message.encode(ENCODING))


def handle_client(client):
	while True:
		try:
			msg=client.recv(BUFSIZE).decode(ENCODING)
			print(msg)
			broadcast(f'{client.raddr} sends: msg',client)
		except:
			print(clients)
			clients.remove(client)
			client.close()


while True:
	(client, port)=server.accept()
	print(f'Client is connected {port}')

	clients.append(client)
	print(f'clients len: {len(clients)}')

	tr = threading.Thread(target=handle_client,args=(client,))
	tr.start()









