
# card.py
#   银行卡:
#       卡号,密码,余额,是否锁定

class Card:
    def __init__(self, card_id, passwd, money, is_lock = False):
        self.card_id = card_id
        self.passwd = passwd
        self.money = money
        self.is_lock = is_lock

    def __str__(self):
        return f'卡号:{self.card_id},余额:{self.money}, 锁定:{self.is_lock}'
