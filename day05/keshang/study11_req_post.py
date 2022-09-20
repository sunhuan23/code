import requests

# url = "https://wanandroid.com/user/login"
# data = {"username": "ymw001", "password": "123456"}
# re = requests.post(url=url,data=data)
# print(re.status_code)
# print(re.text)
# print(re.json())

url = 'https://www.wanandroid.com/user/register'
data = {'username':'liangchao03','password':'123456','repassword':'123456'}
re = requests.post(url=url,data=data)
print(re.text)