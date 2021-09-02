from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


class HttpGetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
        self.wfile.write('<body>Был получен GET-запрос.</body></html>'.encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        #self.wfile.write('<html><head><meta charset="utf-8">'.encode())
       # self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
        self.wfile.write('<body>POST - Request</body></html>'.encode())


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
  server_address = ('127.0.0.1', 8000)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()
run(handler_class=HttpGetHandler)

