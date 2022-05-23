from http.server import HTTPServer,BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    # setup header
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()

    # setup body and send the response
    response_body = '<h1>Server is working!</h1>'.encode('utf-8')
    self.wfile.write(response_body)

if __name__=='__main__':
  # make server address
  ip = '127.0.0.1'
  port = 8080
  server_address = (ip, port)

  # instantiate the server
  httpd = HTTPServer(server_address, RequestHandler)

  # start server to listen for client's connections
  print(f'HTTP Server is listening on {ip}:{port}')
  httpd.serve_forever()