import json
data = '{"data":{"admin":false,"chapterTops":[],"coinCount":3282,"collectIds":[17956,22665],"email":"","icon":"","id":36899,"nickname":"ymw001","password":"","publicName":"ymw001","token":"","type":0,"username":"ymw001"},"errorCode":0,"errorMsg":""}'
print(data)
print(type(data))
# json转字典
data1 = json.loads(data)
print(data1)
print(type(data1))

data2 = {"name": "小红", "age": 18, "对象": None}
print(data2)
print(type(data2))
# 字典转json
data3 = json.dumps(data2,ensure_ascii=False)
print(data3)
print(type(data3))