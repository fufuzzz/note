import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}

# 1,创建session对象
session = requests.session()

# 2,通过session对象模拟用户登录

url = ''

data = {


}

# 通过session对象发送post请求
# 如果请求的账号没有问题,会把sessionid保存在session对象中
session.post(url, data=data)

# 3,通过session对象可以访问任何需要登录才能访问登录的界面
res = session.get(url='https://cn.hoyoyo.com/my_account~index.html', headers=headers)

with open('hyy.htm', 'w', encoding='utg-8') as fp:
    fp.write(res.text)



# con = requests.get(url='https://cn.hoyoyo.com/my_account~index.html', headers=headers)
# with open('hyy.htm', 'w', encoding='utg-8') as fp:
#     fp.write(con.text)