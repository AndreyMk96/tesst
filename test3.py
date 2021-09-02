import requests
url = 'http://localhost:8000'
requests.get(url)
res = requests.post(url)
res.encoding = 'utf - 8'
print(res.text)