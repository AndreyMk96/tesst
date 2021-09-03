import requests
url = 'http://localhost:8000'
requests.get(url)
#res = requests.post(url, data = "aaa")
res = requests.get(url)
res.encoding = 'utf - 8'
print(res.text)