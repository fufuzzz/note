# bank.py
#   银行功能
#       属性:
#       方法: 开户,查询,存款,取款,转账,改密,锁卡,解锁,补卡,销户,退出
from user import User
from card import Card
import pickle
import random

import os


class Bank:
    # 属性
    def __init__(self):
        # 保存千锋银行的所有用户:
        #   key: 保存卡号
        #   value: 保存用户对象
        self.user_dict = {}
        # 存储银行账户的文件
        self.path = 'users.txt'
        # 启动银行系统后,立刻获取所有账户信息
        self.__get_users()

        # 显示所有用户
        self.show_users()

    # 显示所有用户信息
    def show_users(self):
        for k, v in self.user_dict.items():
            print(k, v)

    # 获取文件中对的所有用户
    def __get_user(self):
        if os.path.exists(self.path):
            fp = open(self.path, 'rb')
            self.user_dict = pickle.load(fp)
            fp.close()

    # 存储所有用户到文件中
    def __save_users(self):
        fp = open(self.path, 'wb')
        pickle.dumps(self.user_dict, fp)
        fp.close()



    # 开户
    def create_user(self):
        # 1. 先创建卡对象
        card_id = self.__gen_cardid()
        # print(card_id)
        print('->成功生成卡号')

        # 设置密码: 思考如何确认密码
        passwd = input('请输入密码:')
        # 设置余额
        money = float(input('请输入余额'))
        # 创建银行卡对象
        card = Card(card_id, passwd, money)
        print(card)
        # 2. 创建用户对象
        name = input('请输入开户账号名字')
        idcard = input('请输入开户账号身份号码')
        phone = input('请输入手机号码')

        user = User(name, card, idcard, phone)
        print("user:", user)

        # 3. 将新用户, 保存到user_dict中
        self.user_dict[card_id] = user
        # print('user_dict', self.user_dict)
        # print('*'*60)

        # try:
        #     fp2 = open('1.txt', 'rb')
        #     u = pickle.load(fp2)
        #     for k, v in u.items():
        #         self.user_dict[k] = v
        #     fp = open('1.txt', 'wb')
        #     pickle.dump(self.user_dict, fp)
        #     fp2.close()
        #     fp.close()
        # except:
        #     fp = open('1.txt', 'wb')
        #     pickle.dump(self.user_dict, fp)
        #     fp.close()

        # 4.将修改后的user_dict保存到文件
        self.__save_users()


    # 生成随机卡号

    def __gen_cardid(self):
        while True:
            card_id = '88886666'
            for i in range(4):
                card_id += str(random.randint(0, 9))
            # 如果卡号不存在,则返回
            if card_id not in self.user_dict:
                return card_id

    # 输入卡号密码
    def input_cardid(self):
        card_id = input('输入卡号:')
        if card_id in self.user_dict:
            print('-->您的卡号不存在')
            return

        for i in range(3):
            passwd = input('输入卡密码:')
            if passwd == self.user_dict[card_id].card.passwd:
                return card_id
            print('密码错误,请重试...')
        return

    # 查询
    def search(self):
        card1 = input('输入卡号:')
        passwd1 = input('输入卡密码:')
        fp2 = open(f'1.txt', 'rb')
        u = pickle.load(fp2)
        if card1 in u:
            if u[card1].card.passwd == passwd1:
                print(f'余额:{u[card1].card.money}')

    # 存款

    def save_money(self):
        # card1 = input('输入卡号:')
        # passwd1 = input('输入卡密码:')
        # fp2 = open(f'1.txt', 'rb')
        # u = pickle.load(fp2)
        # if card1 in u:
        #     if u[card1].card.passwd == passwd1:
        #         money1 = float(input('输入存储的金额:'))
        #         u[card1].card.money += money1
        #         print(f'当前余额为:{u[card1].card.money}')
        # fp3 = open('1.txt', 'wb')
        # pickle.dump(u, fp3)
        # fp2.close()
        # fp3.close()
        card_id = self.input_cardid()
        if not card_id:
            return
        money = float(input('输入存储的金额:'))
        self.user_dict[card_id].card.money += money
        self.__save_users()
        self.show_users()

    # 取款
    def draw_money(self):
        card1 = input('输入卡号:')
        passwd1 = input('输入卡密码:')
        fp2 = open('1.txt', 'rb')
        u = pickle.load(fp2)
        if card1 in u:
            if u[card1].card.passwd == passwd1:
                money1 = float(input('输入取出的金额:'))
                u[card1].card.money -= money1
                print(f'当前余额为:{u[card1].card.money}')
        fp3 = open('1.txt', 'wb')
        pickle.dump(u, fp3)
        fp2.close()
        fp3.close()

    # 转账
    def transfer_money(self):
        card1 = input('输入卡号:')
        passwd1 = input('输入卡密码:')
        fp2 = open('1.txt', 'rb')
        u = pickle.load(fp2)
        if card1 in u:
            if u[card1].card.passwd == passwd1:
                card2 = input('输入转入卡号:')
                money1 = float(input('输入转账金额:'))
                u[card1].card.money -= money1
                u[card2].card.money += money1
                print(f'当前余额为:{u[card1].card.money}')
        fp3 = open('1.txt', 'wb')
        pickle.dump(u, fp3)
        fp2.close()
        fp3.close()

    # 改密
    def modify_passwd(self):
        card1 = input('输入卡号:')
        passwd1 = input('输入卡密码:')
        fp2 = open('1.txt', 'rb')
        u = pickle.load(fp2)
        if card1 in u:
            if u[card1].card.passwd == passwd1:
                passwd2 = input('输入需要改的密码:')
                u[card1].card.passwd = passwd2
                print(f'修改密码后的密码是:{u[card1].card.passwd}')
        fp3 = open('1.txt', 'wb')
        pickle.dump(u, fp3)
        fp2.close()
        fp3.close()

    # 锁卡
    def lock_card(self):
        card1 = input('输入卡号:')
        passwd1 = input('输入卡密码:')
        fp2 = open('1.txt', 'rb')
        u = pickle.load(fp2)
        if card1 in u:
            if u[card1].card.passwd == passwd1:
                u[card1].card.is_lock = True
                print('已锁定')
        fp3 = open('1.txt', 'wb')
        pickle.dump(u, fp3)
        fp2.close()
        fp3.close()

    # 解锁
    def unlock_card(self):
        card1 = input('输入卡号:')
        passwd1 = input('输入卡密码:')
        fp2 = open('1.txt', 'rb')
        u = pickle.load(fp2)
        if card1 in u:
            if u[card1].card.passwd == passwd1:
                u[card1].card.is_lock = False
                print('已解锁')
        fp3 = open('1.txt', 'wb')
        pickle.dump(u, fp3)
        fp2.close()
        fp3.close()

    # 补卡
    def makeup_card(self):
        pass

    # 销户
    def del_user(self):
        card1 = input('输入卡号:')
        passwd1 = input('输入卡密码:')
        fp2 = open('1.txt', 'rb')
        u = pickle.load(fp2)
        if card1 in u:
            if u[card1].card.passwd == passwd1:
                u.pop(card1)
                print(f'已经删除卡号是{card1}的银行卡账户信息')
        fp3 = open('1.txt', 'wb')
        pickle.dump(u, fp3)
        fp2.close()
        fp3.close()
