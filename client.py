import requests
url = 'http://localhost:8000'
#res = requests.post(url, data = "qwerty", params='3')
res = requests.get(url, params = '2')
res.encoding = 'utf - 8'
print(res.text)
