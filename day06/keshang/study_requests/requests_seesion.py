import requests

url1 = "https://wanandroid.com/user/login"
data = {"username": "ymw001", "password": "123456"}
s = requests.session()
re1 = s.post(url=url1,data=data)

url2 = "https://wanandroid.com//user/lg/userinfo/json"
re2 = s.get(url=url2)
print(re2.text)