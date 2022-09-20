import smtplib,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from common.ReadConfig import ReadConfig
"""
定义一个发送邮件的类
    定义一个初始化方法
        获取发送人
        获取接收人
        获取服务器
        获取标题
        获取用户名
        获取授权码
        获取文件地址
    定义一个发送文本的方法
        
    定义一个发送带附件的邮件方法
    定义一个对外使用的发送邮件方法
    
"""
class SendEmail:
    def __init__(self,**kwargs):
        self.sender = kwargs['sender']
        self.receiver = eval(kwargs['receiver'])
        self.t = time.strftime(time.localtime())
        self.subject = kwargs['subject'] + self.t
        self.smtpserver = kwargs['smtpserver']
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.content = kwargs['content']
        self.filename = kwargs['filename']
    def send_text(self):
        msg = MIMEMultipart()
        msg.attach(MIMEText(self.content,'plain','utf-8'))
        msg['subject'] = Header(self.subject,'utf-8')
        msg['From'] = self.sender
        msg['To'] = ''.join(self.receiver)
        return msg
    def send_file(self,report_path):
        with open(report_path,'rb') as f:
            email_body = f.read()
        att = MIMEText(email_body,'palin','utf-8')
        att['content-type'] = 'application/octet-stream'
        att['Content-Disposition'] = f'attachment;filename={self.filename}'
        msg = self.send_text()
        msg.attach(att)
        return msg
    def sendEmail(self,file = None):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtpserver)
        smtp.login(self.username,self.password)
        try:
            if file == None:
                smtp.sendmail(self.sender,self.receiver,self.send_text().as_string())
            else:
                smtp.sendmail(self.sender,self.receiver,self.send_file(file).as_string())
        except:
            print('邮件发送失败')
        else:
            print('邮件发送成功')
        finally:
            smtp.close()
rc = ReadConfig()
data_dict = rc.readConfig('email')
print(data_dict)
sE = SendEmail(**data_dict)