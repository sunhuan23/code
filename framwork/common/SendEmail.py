import smtplib,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from common.ReadConfig import ReadConfig

"""
1、定义一个发送邮件的类
    1、1 定义一个初始化方法
        发送人邮箱
        收件人邮箱
        邮箱服务器地址
        邮件标题
        邮件内容
        邮件附件名称
        登录邮箱
        邮箱授权码
    1、2 定义一个发送文本邮件的方法
        实例化MIMEMultipart
        添加邮件内容
        添加邮件标题
        返回邮件
    1、3 定义一个带附件的邮件方法，报告路径
        打开报告
        读报告
        将报告内容添加为附件内容
        添加格式
        添加附件名称
        将附件添加至邮箱
        返回邮箱
    1、4 定义一个连接服务器的方法，报告路径默认为None
        实例化smtplib
        连接服务器
        登录
        判断报告路径是否为空
        是，只发送纯文本邮件
        否，发送带附件邮件
"""
# 1、定义一个发送邮件的类

class SendEmail:
#     1、1 定义一个初始化方法
    def __init__(self,**kwargs):
#         发送人邮箱
        self.sender = kwargs['sender']
#         收件人邮箱
        self.receiver = eval(kwargs['receiver'])
#         邮箱服务器地址
        self.smtpserver = kwargs['smtpserver']
#         邮件标题
        self.t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        self.subject = kwargs['subject'] + self.t
#         邮件内容
        self.content = kwargs['content']
#         邮件附件名称
        self.filename = kwargs['filename']
#         登录邮箱
        self.username = kwargs['username']
#         邮箱授权码
        self.password = kwargs['password']
#     1、2 定义一个发送文本邮件的方法
    def send_text(self):
#         实例化MIMEMultipart
        msg = MIMEMultipart()
#         添加邮件内容
        msg.attach(MIMEText(self.content,'plain','utf-8'))
#         添加邮件标题
        msg['subject'] = Header(self.subject,'utf-8')
        msg['From'] = self.sender
        msg['To'] = ','.join(self.receiver)
        return msg
#         返回邮件
#     1、3 定义一个带附件的邮件方法，报告路径
    def send_file(self,file_path):
        #         打开报告

        with open(file_path, 'rb') as f:
        #         读报告
            email_body = f.read()
        #         将报告内容添加为附件内容
        att = MIMEText(email_body, 'plain', 'utf-8')
        #         添加格式
        att['content-type'] = 'application/octet-stream'
        #         添加附件名称
        att['Content-Disposition'] = f'attachment;filename={self.filename}'
        #         将附件添加至邮箱
        msg = self.send_text()
        msg.attach(att)
        return msg
        #         返回邮箱
#     1、4 定义一个连接服务器的方法，报告路径默认为None
    def sendEmail(self,filepath=None):
#         实例化smtplib
        smtp = smtplib.SMTP()
#         连接服务器
        smtp.connect(self.smtpserver)
#         登录
        smtp.login(self.username,self.password)
#         判断报告路径是否为空
        try:
            if filepath is None:
    #         是，只发送纯文本邮件
                smtp.sendmail(self.sender,self.receiver,self.send_text().as_string())
            else:
    #         否，发送带附件邮件
                smtp.sendmail(self.sender,self.receiver,self.send_file(filepath).as_string())
        except:
            print('邮件发送失败')
        else:
            print('邮件发送成功')
        finally:
            smtp.quit()
rc = ReadConfig()
kwags = rc.get_config('email')
sE = SendEmail(**kwags)