import requests
url = 'http://localhost:8000'
#res = requests.post(url, data = "070909111", params='2')
res = requests.get(url, params = '3')
res.encoding = 'utf - 8'
print(res.text)
