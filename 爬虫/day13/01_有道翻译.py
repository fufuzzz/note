import random
import time
import hashlib
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'cookie': 'OUTFOX_SEARCH_USER_ID=1954360768@113.88.86.209; JSESSIONID=aaabOb7IJaY97_nbiqJHx; OUTFOX_SEARCH_USER_ID_NCOO=259226136.23004508; ___rl__test__cookies=1616572896543',
    'Referer': 'http://fanyi.youdao.com/'

}
def get_data(word):
    ts = int(time.time()*1000)
    salt = str(ts) + str(random.randint(0, 9))
    strs = "fanyideskweb" + word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
    md5 = hashlib.md5()
    md5.update(strs.encode())
    sign = md5.hexdigest()
    data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': ts,
        'bv': 'cda1e53e0c0eb8dd4002cefc117fa588',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    req = requests.post(url=url, data=data, headers=headers)

    print(req.json())

get_data('你好')