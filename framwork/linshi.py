# from appium import webdriver
# def startUp():
#     print("启动中")
#     # 启动参数设置成dict数据格式
#     desire_caps = {
#         # 通过adb devices获取,此处是模拟器所以填写的是ip和port
#         "deviceName": "295f8761",
#         # "deviceName": "192.168.3.15:21503",
#
#         # 被测系统决定是Android还是ios
#         "platformName": "Android",
#         # 系统版本:通过查看被测的系统的设置确定
#         "platformVersion": "11",
#         # 包名需进入APP安装包路径通过命令查看:aapt dump badging jinritoutiao.apk |findstr package
#         "appPackage": "com.ss.android.article.news",
#         # activity名:需进入app安装包路径通过命令查看:aapt dump badging jinritoutiao.apk |findstr activity
#         "appActivity": "com.ss.android.article.news.activity.MainActivity",
#         # 在此会话前不要重置应用程序
#         "noReset": True,
#         # 解决输入中文的问题,否则不能用sendkeys输入中文
#         "unicodeKeyboard": True,
#         # 'newCommandTimeout': 600
#         'automationName': 'UiAutomator2'
#     }
#     # 3-启动app(第一个参数输入appiumserver的服务器地址,服务器的端口号默认4723,第二个参数输入启动参数)
#     driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
#     print("启动完成,等待6s")
# startUp()

l = lambda a,b : a +b
print(l(1,2))

