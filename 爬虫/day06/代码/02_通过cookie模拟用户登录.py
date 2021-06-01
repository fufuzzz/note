import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'Cookie': ''

}


res =  requests.get(url='https://cn.hoyoyo.com/my_account~index.html', headers=headers)

with open('hyy2.html', 'w',  encoding='utf-8') as fp:
    fp.write(res.text)