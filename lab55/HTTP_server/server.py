""" Example using http.server built-in module

	Reference :https://docs.python.org/3/library/http.server.html

"""

import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
	def _set_response(self, status_code):
		self.send_response(status_code)
		self.send_header("Content-type", "text/html")
		self.send_header("IvaHeader", "test")
		self.send_header("Serer", "My Simple HTTP server ")
		self.end_headers()


	# def do_GET(self):
	# 	self._set_headers()
	# 	self.wfile.write(self._html("hi!"))

	def do_GET(self):
		print(f'Request: {self.request}')
		# print(f'requestline: {self.requestline}')
		# print(f'path: {self.path}')
		# self.path = '/tests.pdf'
		# Make response body:
		if self.path =="/":
			file = root + self.path + 'index.html'

		else :
			pass
			# TODO: finish in labs
			# if file_path exists:

			# body = open(file, 'rb').read()
			# status_code = 200

			# body = f'no such file: {self.path}'.encode('utf-8')
			# status_code = 404

		# setup response
		self._set_response(status_code)
		print(f'body: {body}')

		# send responce body
		self.wfile.write(body)

	def do_HEAD(self):
		self._set_headers()

	def do_POST(self):
		# Doesn't do anything with posted data
		self._set_headers()
		self.wfile.write(self._html("POST DONE!"))


if __name__ == "__main__":
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
		default='./front-end/',
		help="server root path",
	)

	args = parser.parse_args()
	addr,port,root = args.listen, args.port, args.root

	server_address = (addr, port)

	httpd = HTTPServer(server_address, RequestHandler)

	try:
		print(f"Starting httpd server on {addr}:{port}")
		httpd.serve_forever()

	except KeyboardInterrupt:
		pass

	httpd.server_close()
	print('Stopping httpd...\n')
	exit()