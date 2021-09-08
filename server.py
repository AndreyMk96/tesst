from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import datetime
from urllib.parse import urlparse
import temp
import json
import mysql.connector

class HttpGetHandler(BaseHTTPRequestHandler):
    """Класс используется для обработки HTTP-запросов, поступающих на сервер."""

    #функция для обработки GET-Запросов
    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        result = urlparse(self.path)
        par = int(result.query)
        self.end_headers()

        #Если передан параметр 1, происходит подключение к БД MySQL, и отправка
        #данных из БД
        if par == 1:
            mydb = mysql.connector.connect(
                host="localhost", user="Andrey", password="12345678", database="workbase"
            )
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM new_table")
            for k,v in cursor.fetchall():
                self.wfile.write((k + ' ' + str(v) + '\n').encode())

        # Если передан параметр 2, происходит подключение к БД Redis, и отправка
        # данных из БД
        elif par == 2:
            r = temp.open_redis()
            for k in r.keys():
                self.wfile.write(k +  ' '.encode() + r.get(k) + '\n'.encode())

        # Если передан параметр 3, отправка данных из data.json
        elif par == 3:
            with open('data.json') as f:
                templates = json.load(f)
                self.wfile.write(json.dumps(templates).encode('utf-8'))

        # во всех остальных случаях сообщаем пользователю что передан неверный параметр
        else:
            self.wfile.write('Передан неизвестный параметр'.encode())


    #Функция для обработки POST - Запросов
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        result = urlparse(self.path)
        par = int(result.query)
        self.end_headers()

        # Если передан параметр 1, происходит подключение к БД MySQL, и запись
        # данных в БД
        if par == 1:
            mydb = mysql.connector.connect(
                host="localhost", user="Andrey", password="12345678", database="workbase"
            )
            cursor = mydb.cursor()
            cursor.execute("""INSERT INTO new_table(data, other_info)
                                 VALUES ('%s', '%s')
                                 """ % (post_data.decode("utf-8"),datetime.datetime.now()))

            mydb.commit()
            temp.load_json(post_data.decode("utf-8"), "POST", 200)
            self.wfile.write('Данные записаны в MySQL'.encode())

        # Если передан параметр 2, происходит подключение к БД Redis, и запись
        # данных в БД
        elif par == 2:
            r = temp.open_redis()
            r.set(post_data.decode("utf-8"),str(datetime.datetime.now()))
            temp.load_json(post_data.decode("utf-8"), "POST", 200)
            self.wfile.write('Данные занесены в redis'.encode())

        #во всех остальных случаях сообщаем пользователю что передан неверный параметр
        else:
            self.send_response(400)
            temp.load_json(post_data.decode("utf-8"), "POST", 400)
            self.wfile.write('Передан неизвестный параметр'.encode())


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
  server_address = ('127.0.0.1', 8000)
  httpd = server_class(server_address, handler_class)
  try:
      temp.clear_json()
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()

run(handler_class=HttpGetHandler)

