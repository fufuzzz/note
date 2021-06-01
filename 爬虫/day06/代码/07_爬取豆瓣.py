import requests
import re
import multiprocessing
import threading
import json


def get_douban(p):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        'Cookie': 'bid=TIrLlMya-O0; douban-fav-remind=1; __yadk_uid=Nmgucbd7ztoDuCx455ijWHU4nDuTMzAY; __gads=ID=de9bd27630a70c97-22e9b5b162c60078:T=1615598791:RT=1615598791:S=ALNI_MYhJpiARg0T8bVqiGVbH2PYC3HRxA; __utmz=30149280.1615598793.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; ll="118282"; push_noty_num=0; push_doumail_num=0; dbcl2="44073017:NGiESUtXIu4"; ck=9AaV; __utma=30149280.31930422.1615598793.1615801106.1615808106.3; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1615808399%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DEBXdwquLX2EBsjKpdxl_lROzNEXwqofYEKB6MBLal_fKS9xukc_GznBimvli0Gnw%26wd%3D%26eqid%3De41dd89e0001525500000004604f34e7%22%5D; _pk_ses.100001.8cb4=*; __utmv=30149280.4407; ct=y; __utmt=1; __utmt_douban=1; _pk_id.100001.8cb4=9fae8e9e1f715e1b.1615598791.3.1615810026.1615803625.; __utmb=30149280.19.10.1615808106'
    }
    con = requests.get(url='https://movie.douban.com/chart', headers=headers)
    con.encoding = 'utf-8'

    # print(con.text)
    # 范围
    name = re.findall(r'<a.*?title="(.*?)">', con.text, re.S)
    url = re.findall(r'<a class="nbg" href="(.*?)".*?title.*?>.*?</a>', con.text, re.S)
    actor = re.findall(r'<p class="pl">(.*?)</p>.*?<div', con.text, re.S)
    score = re.findall(r'<span class="rating_nums">(.*?)</span>.*?<span.*?', con.text, re.S)
    num = re.findall(r'</span>.*?<span class="pl">(.*?)</span>.*?</span>', con.text, re.S)
    # print(name)  # ['同学麦娜丝', '发财日记', '孤味', '紧急救援', '无依之地', '大红包', '亲爱的房客', '无声', '我很在乎', '白虎']
    # print(actor)
    # print(scoure)
    # print(num)
    director_list = []
    sort_list = []
    for i in range(p):
        con2 = requests.get(url=url[i], headers=headers)
        con2.encoding = 'utf-8'

        director = re.findall(r'<div id="info">.*?rel="v:directedBy">(.*?)</a>', con2.text, re.S)
        sort = re.findall(r'</span> <span property="v:genre">(.*?)</span>.*?<br/>', con2.text, re.S)

        director_list.append(director[0])
        sort_list.append(sort[0])
    # print(sort_list)
    # print(director_list)

    data_list = []
    for name, director, actor, sort, score, num in zip(name, director_list, actor, sort_list, score, num):

        data_list.append({
            '名称': name,
            '导演': director,
            '演员': actor,
            '类型': sort,
            '评分': score,
            '评分人数': num
        })
    # print(len(data_list))
    with open('douban.json', 'w', encoding='utf-8') as fp:
        json.dump(data_list, fp, ensure_ascii=False)



if __name__ == '__main__':

    for i in range(10):
        threading.Thread(target=get_douban, args=(i,)).start()
    # get_douban()
