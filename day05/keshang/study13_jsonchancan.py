import requests
import json

url = 'http://httpbin.org/post'

data = {"username": "ymw001", "password": "123456"}
# 方式一：
# 直接将字典传给json
# re = requests.post(url=url,json=data)
# print(re.text )

# 方式二：
# 字典转json
data1 = json.dumps(data)
re1 = requests.post(url=url,data=data1)
print(re1.text)