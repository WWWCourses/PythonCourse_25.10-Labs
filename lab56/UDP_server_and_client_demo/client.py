import socket

HOST = '127.0.0.1'
PORT = 9000
BUFSIZE = 1024

# create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send message to (HOST,PORT)
msg = 'Hello from Client'
client.sendto(msg.encode('utf-8'), (HOST,PORT))

# receive message from server:
msg = client.recv(BUFSIZE)
print(msg.decode('utf-8'))

client.close()