""" Example using http.server built-in module

	Reference :https://docs.python.org/3/library/http.server.html

"""

import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler, socketserver
import os
# from utils import SERVER_ROOT_PATH
import re

class RequestHandler(BaseHTTPRequestHandler):
	def __init__(self, request: bytes, client_address: tuple[str, int], server: socketserver.BaseServer) -> None:
		super().__init__(request, client_address, server)

		print(f'Received request from: {self.client_address}')
		# print(f'Request: {self.request}')

	def _set_headers(self,status_code):
		self.send_response(status_code)
		self.send_header("Content-type", "text/html")
		self.send_header("Server", "My Simple HTTP server ")
		self.end_headers()

	def _get_request_headers(self):
		print(self.headers)


	def do_GET(self):
		# Make response body:
		# PATH: /index.html?userName=Ada&pass=123
		if self.path =="/":
			file = httpd_root+self.path+'index.html'
		else:
			# get query params, if any
			rgex = re.compile(r'^(\/[^?]+)\??(.+)?$')
			m = rgex.search(self.path)
			if m:
				file_path = m.group(1)
				query = m.group(2)
				print(f'file_path: {file_path}, QUERY: {query}')
				# do something with query

			# get file
			file = os.path.normpath(httpd_root+'/'+ self.path)

		try:
			body = open(file, 'rb').read()
			status_code = 200
		except:
			# return 404 if file did not exists
			body = f'no such file: {file}'.encode('utf-8')
			status_code = 404

		# setup response
		self._set_headers(status_code)

		# send responce body
		self.wfile.write(body)

	def do_HEAD(self):
		self._set_headers(200)

	def do_POST(self):
		self._set_headers(200)
		content_length = int(self.headers.get('content-length', 0))
		post_body = self.rfile.read(content_length)
		print(f'post_body:{post_body}')
		self.wfile.write(f'received post request:<br>{post_body}'.encode('utf-8'))

def get_args():
	parser = argparse.ArgumentParser(description="Run a simple HTTP server")
	parser.add_argument(
		"-l",
		"--listen",
		default="localhost",
		help="IP address on which the server listens",
	)
	parser.add_argument(
		"-p",
		"--port",
		type=int,
		default=8000,
		help="port on which the server listens",
	)
	parser.add_argument(
		"-r",
		"--root",
		default='./front-end',
		help="server root path",
	)

	args = parser.parse_args()
	return args

if __name__ == "__main__":
	args = get_args()

	addr,port,httpd_root = args.listen, args.port, args.root
	# HTTPD_PATH=os.path.join(SERVER_ROOT_PATH,root)

	server_address = (addr, port)

	httpd = HTTPServer(server_address, RequestHandler)

	try:
		print(f"Starting httpd server on {addr}:{port}.Serving from {httpd_root}")
		httpd.serve_forever()

	except KeyboardInterrupt:
		pass

	httpd.server_close()
	print('Stopping httpd...\n')
	exit()