import redis

r = redis.StrictRedis(
    host = "redis-15543.c279.us-central1-1.gce.cloud.redislabs.com",#:15543",
    port=15543,  # из Endpoint
    password='59XKlVEiX7BapxV8TOFwCu6hhIiQHe3p'  # ваш пароль
)
#r.set("c","d")
for k in r.keys():
    print(k.decode('utf-8'), r.get(k).decode('utf-8'))