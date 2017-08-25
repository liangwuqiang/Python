# coding=utf-8
import json

with open('temp.txt') as f:
    content = f.read()

print('content', content)
print(type(content))

jsonData = json.loads(content)

print(jsonData)
print(type(jsonData))
