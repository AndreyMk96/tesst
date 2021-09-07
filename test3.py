import json
data = {'a':'b', 'c':'d'}

with open('data.json', 'w') as f:
    json.dump(data ,f)


with open('data.json') as f:
    templates = json.load(f)

print(templates)
