
# 发送邮件
import smtplib
from email.mime.text import MIMEText

# 邮箱
# 邮件
# 163邮箱的服务器地址: smtp.163.com
# smtp端口: 25
# 邮箱账号: niejeff@163.com
# 授权密码: 123456abcde

smtp_server = 'smtp.163.com'
smtp_port = 25

from_email = 'niejeff@163.com'
auth_code = '123456abcde'

# 1.创建邮件
mail = MIMEText('年轻人不讲武德')
mail['Subject'] = '马保国同志'
mail['From'] = from_email
mail['To'] = 'nijeff@16963.com'

# 2.登录邮箱,然后发送邮件
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.login(from_email, auth_code)

smtp.sendmail(from_email, ['niejeff@163.com', '1223691614@qq.com'], mail.as_string())

# 关闭
smtp.close()
