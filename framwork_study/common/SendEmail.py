import smtplib, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from common.ReadConfig import ReadConfoig
"""
定义一个发送邮件的类
    定义一个初始化方法
        发件人
        收件人
        服务器地址
        登录用户名
        授权码
        邮件标题
        邮件内容
        附加名称
    定义一个发送文本邮件的方法
        初始化mimemultipart
        添加文本信息
        添加标题
        添加发件人
        添加收件人
        将邮件返回
    定义一个发送带附件的邮件方法
        添加附件信息
        设置附件格式
        设置附件名称
        将附件添加到邮件
        将邮件返回
    定义一个连接服务器的方法
        实例化smtplib
        连接服务器
        登录服务器
        发送邮件
"""
class SendEmail:
    def __init__(self,**kwargs):
        self.sender = kwargs['sender']
        self.receiver = eval(kwargs['receiver'])
        self.smtpserver = kwargs['smtpserver']
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        self.subject = kwargs['subject'] + self.t
        self.content = kwargs['content']
        self.filename = kwargs['filename']
    def add_text(self):
        msg = MIMEMultipart()
        msg.attach(MIMEText(self.content,'plian','utf-8'))
        msg['subject'] = Header(self.subject,'utf-8')
        msg['From'] = self.sender
        msg['To'] = ','.join(self.receiver)
        return msg
    def add_file(self,filepath):
        with open(filepath,'rb') as f:
            email_body = f.read()
        att = MIMEText(email_body,'plian','utf-8')
        att['content-type'] = 'application/octet-stream'
        att['Content-Disposition'] =f'attachment;filename={self.filename}'
        msg = self.add_text()
        msg.attach(att)
        return msg
    def sendemail(self,filepath=None):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtpserver)
        smtp.login(self.username,self.password)
        try:
            if filepath ==None:
                smtp.sendmail(self.sender,self.receiver,self.add_text().as_string())
            else:
                smtp.sendmail(self.sender,self.receiver,self.add_file(filepath).as_string())
        except:
            print('邮件发送失败')
        else:
            print('邮件发送成功')
        finally:
            smtp.close()
rc = ReadConfoig()
data_dict = rc.readConfig('email')
sE = SendEmail(**data_dict)



