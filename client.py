import requests
url = 'http://localhost:8000'
#res = requests.post(url, data = "hiiiiiiii", params='1')
res = requests.get(url, params = '3')
res.encoding = 'utf - 8'
print(res.text)
