import requests
url = 'http://localhost:8000'
res = requests.post(url, data = "qwerty1234", params='3')
# = requests.get(url, params = '4')
res.encoding = 'utf - 8'
print(res.text)
