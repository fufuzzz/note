import requests
import random


def send_sms(mobile, vcode):
    '''
    发送短信

    :param mobile: 手机号码
    :param vcode: 验证码
    :return:
    '''
    url = 'https://open.ucpaas.com/ol/sms/sendsms'
    # 参数
    params = {
        'sid': '20ed44a8a295a6da82bbbd5564c3e406',
        'token': 'f4b872aaa462de936d7bbcc90fe688c8',
        'appid': 'bef693ef02484fdd84cd048e1634e0f6',

        'templateid': '585247',  # 模板id
        'param': vcode,  # 验证码
        'mobile': mobile,  # 手机号码
    }
    # 发送短信
    res = requests.post(url, json=params)
    print(res.text)


def random_vcode():
    '''
    生成随机验证码
    :return: 返回验证码
    '''
    vcode = ''
    for i in range(6):
        vcode += str(random.randint(0, 9))
    return vcode


if __name__ == '__main__':
    vcode = random_vcode()
    print("当前验证码:", vcode)
    send_sms('17607042334', vcode)
