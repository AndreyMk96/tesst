import json
import mysql.connector
import redis
import os

#функция записи в json файл
#происходит запись трех параметров:
#данные, тип запроса, ответ сервера
def load_json(data, type, resp):
    try:
        with open('data.json') as f:
            templates = json.load(f)
        f.close()
        d = {}
    except:
        templates = []
        d = {}

    d["data : "] = data
    d["type : "] = type
    d["status : "] = resp
    templates.append(d)
    with open('data.json', 'w') as f:
        json.dump(templates, f)
    f.close()


#функция подключения к бд Redis
def open_redis():
    r = redis.StrictRedis(
        host="redis-15543.c279.us-central1-1.gce.cloud.redislabs.com",
        port=15543,
        password='59XKlVEiX7BapxV8TOFwCu6hhIiQHe3p'
    )
    return r

#функция очистки json - файла
def clear_json():
    if os.path.exists("data.json"):
        os.remove("data.json")
    open("data.json", 'w')
