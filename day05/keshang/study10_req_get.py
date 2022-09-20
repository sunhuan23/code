# 导包
import requests
url = 'https://www.kuaidi100.com/query'

paylod = {"type": "shunfeng", "postid": "SF1409812533378"}

re = requests.get(url=url,params=paylod)
# 查询状态码
print(re.status_code)
# 查询响应信息
print(re.text)
# 将响应对象转为字典格式
res = re.json()
print(res['message'])
# 查询响应头
print('响应头',re.headers)
# 查看请求头
print('请求头',re.request.headers)
# 查看cookie
print('cookie',re.cookies)
