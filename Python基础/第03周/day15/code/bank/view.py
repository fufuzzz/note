
# view.py
#   显示界面:
#       欢迎界面, 登录界面

import time
# 界面类
class View:

    # 欢迎界面
    @classmethod
    def welcome(cls):
        print('*********************************')
        print('*********************************')
        print('******    欢迎来到千锋银行    ******')
        print('******      版本: V1.0      ******')
        print('******                     ******')
        print('******       贪玩蓝月        ******')
        print('***    渣渣辉: 是兄弟就来砍我    ***')
        print('*********************************')
        print('*********************************')
        time.sleep(1)

    @classmethod
    def login(cls):
        # 模拟用户
        user_dict = {'zhangsan': '123456', 'lisi': '123456'}

        # 用户输入用户名和密码
        # 先输入用户名:
        username = input('请输入用户名:')
        if username not in user_dict:
            print('->您输入的用户名不存在!')
            return
        # 然后输入密码:
        passwd = input('请输入密码:')
        if user_dict[username] != passwd:
            print('->您输入的密码错误')
            return

        # 登录成功
        print('->恭喜您! 登录成功! 正在跳转到银行首页...')
        time.sleep(1)
        return True
    # 银行首页: 主界面
    @classmethod
    def home(cls):
        print('*********************************')
        print('*********************************')
        print('*******    主界面功能     ********')
        print('*******(1)开户     (2)查询********')
        print('*******(3)存款     (4)取款********')
        print('*******(5)转账     (6)改密********')
        print('*******(7)锁卡     (8)解锁********')
        print('*******(9)补卡     (0)销户********')
        print('*******     (q)退出      ********')
        print('*******                  ********')
        print('*********************************')
        print('*********************************')