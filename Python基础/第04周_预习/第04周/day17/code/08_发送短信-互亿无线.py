import requests

# 用户名 查看用户名请登录用户中心->验证码、通知短信->帐户及签名设置->APIID
account = "C80604386"
# 密码 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
password = "密码"
mobile = "138xxxxxxxx"
text = "您的验证码是：121254。请不要把验证码泄露给其他人。"
data = {'account': account,
        'password': password,
        'content': text,
        'mobile': mobile,
        'format': 'json'
        }
url = 'http://106.ihuyi.com/webservice/sms.php?method=Submit',
res = requests.post(url, data=data)
content = res.text
requests.post(url, data=data)

