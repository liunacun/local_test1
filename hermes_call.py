import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


url = 'https://www.hermes.com/ca/en/category/women/bags-and-small-leather-goods/bags-and-clutches/#%7C'
resp = requests.get(url, headers={'Content-Type': 'application/json'})
print(resp.text)
num = 17
# num = resp.json().get('items')

# 你的邮箱地址和密码
sender_email = "liunacun@gmail.com"
sender_password = "isoz wjfs gobl nnli"

# 收件人的邮箱地址
recipient_email = "lnc9387@gmail.com"

# 设置邮件服务器和端口（以 Gmail 为例）
mail_server = "smtp.gmail.com"
mail_port = 587

# 创建带有文本和 HTML 内容的邮件
subject = "Hermes new item in stock"
body = "The current in stock item number is greater than 16"
html_body = "please get online and check the web"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject

text_part = MIMEText(body, "plain")
html_part = MIMEText(html_body, "html")

message.attach(text_part)
message.attach(html_part)

# 满足条件时发送邮件
if num >= 16:
    with smtplib.SMTP(mail_server, mail_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

# 注意：为了使用 Gmail，你可能需要在你的 Gmail 账户中启用“低安全性应用程序访问”或使用应用程序密码。

