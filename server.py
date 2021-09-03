from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import mysql.connector
import datetime
import requests


class HttpGetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        mydb = mysql.connector.connect(
            host="localhost", user="Andrey", password="12345678", database="workbase"
        )
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM other_info")
        #self.wfile.write('<body>Был получен GET-запрос.</body></html>'.encode())
        for k,v in cursor.fetchall():
            self.wfile.write((k + '\n').encode())

    def do_POST(self):
        mydb = mysql.connector.connect(
            host="localhost", user="Andrey", password="12345678", database="workbase"
        )
        cursor = mydb.cursor()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.end_headers()
        cursor.execute("""INSERT INTO other_info(data, other_info)
                             VALUES ('%s', '%s')
                             """ % (post_data.decode("utf-8"),datetime.datetime.now()))

        mydb.commit()
        self.wfile.write('Данные записаны в базу'.encode())


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
  server_address = ('127.0.0.1', 8000)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()
run(handler_class=HttpGetHandler)