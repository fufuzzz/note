import re
import requests
# 爬取 笔趣阁小说网内容, 使用正则表达式取出所有好看的玄幻小说名字:
#   http://www.xbiquge.la/xuanhuanxiaoshuo/

# 爬取网页内容
url = 'http://www.xbiquge.la/xuanhuanxiaoshuo/'

res = requests.get(url)
# print(res.text)
# 网页源码: 字符串(带换行的)
content = res.text

# 使用正则表达式
novel_list = re.findall('<span class="s2"><a.*?>(.*?)</a>', content, re.S)
print(novel_list)
