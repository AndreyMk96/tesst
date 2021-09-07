import requests
url = 'http://localhost:8000'
res = requests.post(url, data = "qwwwwwwwww", params='1')
res = requests.get(url, params = '1')
res.encoding = 'utf - 8'
print(res.text)
