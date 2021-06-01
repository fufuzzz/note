# user.py
#   用户:
#       用户名,银行卡,身份证,手机号


class User:
    def __init__(self, name, card, idcrad, phone):
        self.name = name
        self.card = card
        self.idcard = idcrad
        self.phone = phone

    def __str__(self):
        return f'姓名:{self.name}, 卡号:{self.card.card_id}, 身份证:{self.idcard}, 电话:{self.phone}'
