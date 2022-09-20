import requests

url1 = "https://wanandroid.com/user/login"
data = {"username": "ymw001", "password": "123456"}
re1 = requests.post(url=url1,data=data)
# 查看结果
print(re1.text)
cookie = re1.cookies
print(cookie)
print(re1.headers)
header = {}
header['cookie'] = 'JSESSIONID=B2984920E71A214DE29D49248F2A3B33'


url2 = "https://wanandroid.com//user/lg/userinfo/json"
re2 = requests.get(url=url2,headers=header)
# 查看结果
print(re2.text)

