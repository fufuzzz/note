# main.py
#   项目的入口
from view import View
# form bank import Bank

# 主函数: 代码运行的入口
from Python基础.第03周.day15.code.bank.bank import Bank


def main():
    pass
    # 欢迎界面
    View.welcome()

    # 登录界面
    # is_success = View.login()
    # if not is_success:
    #     print("->登录失败")
    #     return

    # 进入银行首页
    View.home()

    # 用户开始输入数字指令
    my_bank = Bank()

    while True:
        num = input('请输入对应操作编号:')
        if num == '1':  # 开户
            my_bank.create_user()
        elif num == '2':  # 查询
            my_bank.search()
        elif num == '3':  # 存款
            my_bank.save_money()
        elif num == '4':  # 取款
            my_bank.draw_money()
        elif num == '5':  # 转账
            my_bank.transfer_money()
        elif num == '6':  # 改密
            my_bank.modify_passwd()
        elif num == '7':  # 锁卡
            my_bank.lock_card()
        elif num == '8':  # 解锁
            my_bank.unlock_card()
        elif num == '9':  # 补卡
            my_bank.makeup_card()
        elif num == '0':  # 销户
            my_bank.del_user()
        elif num == 'q':  # 退出
            print('->感谢使用,下次再来!')
            break
        else:
            print('->您的输入有误,请重新输入...')


if __name__ == '__main__':
    main()
