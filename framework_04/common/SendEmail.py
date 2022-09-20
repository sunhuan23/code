import smtplib,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from common.ReadConfig import ReadConfig
from common.log import log
"""
定义一个发送邮件的类
    定义一个初始化方法
        获取发件人
        获取收件人
        获取服务器地址
        获取用户名
        获取授权码
        获取内容信息
        获取标题
    定义一个发送纯文本的方法
        实例化MIMEMultipart
        增加文本信息
        添加标题
        添加发件人
        添加收件人
    定义一个发送带有附件的方法，附件路径
        读的方式发开附件
            读取附件内容
        添加附件
        设置附件的格式
        将附件添加到邮件中
    定义一个发送邮件的方法，file
        实例化SMTP
        连接服务器
        登录邮箱
        判断file是否为空
        为空调用发送纯文本的方法
        不为空调用发送带有附件的方法
"""
class SendEmail:
    def __init__(self,**kwargs):
        self.sender = kwargs['sender']
        self.receiver = eval(kwargs['receiver'])
        self.smtpserver = kwargs['smtpserver']
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.content = kwargs['content']
        self.t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        self.subject = kwargs['subject'] + self.t
        self.filename = kwargs['filename']

    def add_text(self):
        msg = MIMEMultipart()
        msg.attach(MIMEText(self.content,'plain','utf-8'))
        msg['subject'] = Header(self.subject,"utf-8")
        msg['From'] = self.sender
        msg['To'] =','.join(self.receiver)
        return msg

    def add_file(self,filepath):
        with open(filepath,'rb') as f:
            email_body = f.read()
        att = MIMEText(email_body,'plain','utf-8')
        att['content-type'] = 'application/octet-stream'
        att['content-Disposition'] =f'attachment;filename={self.filename}'
        msg = self.add_text()
        msg.attach(att)
        return msg

    def sendEmail(self,filepath=None):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtpserver)
            smtp.login(self.username,self.password)
            if filepath == None:
                smtp.sendmail(self.sender,self.receiver,self.add_text().as_string())
            else:
                smtp.sendmail(self.sender,self.receiver,self.add_file(filepath).as_string())
        except:
            print('邮件发送失败')
        else:
            print('邮件发送成功')
        finally:
            smtp.quit()
rc = ReadConfig()
data = rc.readConfig('email')
log().debug(data)
sE = SendEmail(**data)

