import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}
for i in range(5):
    req = requests.get(url=f'https://tieba.baidu.com/f?kw=lol&fr=ala0&tpl={i * 50}', headers=headers)

    with open(f'.\lol_tieba\lol_tieba{i + 1}.html', 'wb') as fp:
        fp.write(req.content)

