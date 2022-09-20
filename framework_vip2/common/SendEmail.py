import smtplib, time, os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from common.readConfig import ReadConfig

# 定义一个发送邮件的类
class SendEmail:
    def __init__(self,**kwargs):
        # 发送邮箱
        self.sender = kwargs["sender"]
        # 接收邮箱
        self.receiver = eval(kwargs["receiver"])
        # 发送邮件主题
        self.t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.subject =kwargs["subject"] +self.t
        # 发送邮箱服务器
        self.smtpserver = kwargs["smtpserver"]
        # 发送邮箱用户/授权码
        self.username = kwargs["username"]
        self.password = kwargs["password"]
        # 发送内容
        self.content = kwargs["content"]

    # 读取html文件内容
    def read_html(self,file):
        with open(file,'rb') as f:
            mail_body = f.read()
            #  组装邮件内容和标题
#             添加附件内容
            att = MIMEText(mail_body,'plain','utf-8')
            att['content-type'] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename=report.html'
            msg = self.add_text()
            msg.attach(att)
            return msg
        # 添加邮件的文本内容
    def add_text(self):
        msg = MIMEMultipart()
        msg.attach(MIMEText(self.content, 'plain', 'utf-8'))
        msg['Subject'] = Header(self.subject, 'utf-8')
        msg['From'] = self.sender
        msg['To'] =','.join( self.receiver)
        return msg
#     连接服务器
    def connection_server(self,file=None):
        try:
            smtp = smtplib.SMTP()
            # 2--连接stmp服务器
            smtp.connect(self.smtpserver)
            # 3--登录邮箱
            smtp.login(self.username, self.password)
            # 4--设置发件人，收件人，邮件内容
            if file is None:
                smtp.sendmail(self.sender, self.receiver, self.add_text().as_string())
            else:
                msg = self.read_html(file)
                smtp.sendmail(self.sender, self.receiver, msg.as_string())
        except:
            print('邮件发送失败')
        else:
            print('邮箱发送成功')
        finally:

            smtp.quit()

if __name__ == '__main__':
    rc = ReadConfig()
    kwargs = rc.get_config('email')
    print(kwargs)
    se = SendEmail(**kwargs)
    print(se.receiver)
    report ="/Users/sunhuan/chenghao/framework_vip2/testReport/2022_08_25_12_01_57report.html"
    se.connection_server(report)


