import multiprocessing
import requests
import re
from lxml import etree
import os
import json

# def get_url(i):
    # with sem:
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

con = requests.get(
    ' https://search.51job.com/list/040000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=',
    headers=headers)

# print(con.text)
html = etree.HTML(con.text)

# 获取<script>
script = re.findall('<script type="text/javascript">.*?window.__SEARCH_RESULT__ = (.*?)</script>', con.text, re.S)

# list = script[0].json()
script = json.loads(script[0])
print(type(script))
contents = ['不好找你妈的']
names = []
companys = []
exes = []
# print(script)
# one_url = script['market_ads'][0]['job_href']
# one_name = script['market_ads'][0]['job_name']
# one_company = script['market_ads'][0]['company_name']
# one_exe = script['market_ads'][0]['attribute_text'][1]
# urls.append(script['market_ads'][0]['job_href'])
names.append(script['market_ads'][0]['job_name'])
companys.append(script['market_ads'][0]['company_name'])
exes.append(script['market_ads'][0]['attribute_text'][1])

# data_list = script['engine_search_result']

for i in range(50):
    req = requests.get(script['engine_search_result'][i]['job_href'], headers=headers)
    req.encoding = 'gbk'
    html = etree.HTML(req.text)
    dsc = html.xpath('//div[@class="bmsg job_msg inbox"]//text()')
    dsc = ''.join(dsc)
    dsc = re.sub('\s{2,}', '', dsc)
    dsc = re.findall('(.*?)微信', dsc, re.S)
    contents.append(dsc)
    names.append(script['engine_search_result'][i]['job_name'])
    companys.append(script['engine_search_result'][i]['company_name'])
    exes.append(script['engine_search_result'][i]['attribute_text'][1])


data_list = []
for name, company, exe, content in zip(names, companys, exes, contents):
    data_list.append({
        'name': name,
        'company': company,
        'exe': exe,
        'content': content
    })
with open('job.json', 'w', encoding='utf-8') as fp:
    json.dump(data_list, fp, ensure_ascii=False)


# if __name__ == '__mian__':
#     sem = multiprocessing.Semaphore(4)
#     for i in range(50):
#         multiprocessing.Process(target=get_url, args=(i, sem)).start()
