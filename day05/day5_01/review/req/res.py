import requests
import json
# url = 'https://wanandroid.com/user/login'
# data = {"username": "liangchao","password": "123456"}
# re = requests.post(url=url,data=data)
#
# # 查看响应状态码
# print(re.status_code)
#
# # 查看响应内容
# print(re.text)
#
# # json转字典
# res = json.loads(re.text)
# print(res)
# print(res['data']['collectIds'][1])

dict1 = {"username": "liangchao","password": "123456"}
# 字典转json
res = json.dumps(dict1)
print(res)

url =  'http://httpbin.org/post'

re = requests.post(url=url,json=res)
print(re.text)
