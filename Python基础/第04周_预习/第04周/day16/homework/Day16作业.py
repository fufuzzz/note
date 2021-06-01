
# 练习
# 匹配中文
import re

chinese_pattern = "游远东"
print(re.search('[\u4e00-\u9fa5]+', chinese_pattern))
# 匹配手机号
phone = '17607042334'
print(re.search('^[1-9]\d{10}$', phone))

# 匹配qq号： 5-11位, 第一位不能为0
qq = '1223691614'
print(re.search('^[1-9]\d{4,10}$', qq))
# 匹配任意一个邮箱   如：jack@163.com，11@qq.com, aaa@sina.com.cn
mail = '1223691614@qq.com'
print(re.search('^\w+@\w+\.\w+$', mail))
# 匹配身份证: 18位，最后一位可能是X
num = '36102419990220001X'
print(re.search('^\d{17}(\d|X)$', num))
# 邮政编码(共6位数字, 第一位不能为0)
print(re.search('^[1-9]\d{5}$', '344200'))
# 用户名(只能使用数字字母下划线, 且数字不能开头, 长度在6-15位)
print(re.search('^[a-zA-Z_]\w{5,14}$', 'dsad_12'))


# 作业
# 简单日期格式 如："2022-11-11"，"2022-1-1"
print(re.search('^\d+-(1|)[1-9]-([1-3]|)[0-9]$', '2020-10-20'))
# 图片文件格式 如："nbb.jpg", "aa.jpeg","aa.png", "aa.gif"
# 提示: 用|
print(re.search('^\w+\.(jpg|jpeg|png|gif)$', 'yyd.jpg'))

# 匹配网址
# 1,匹配下列url网址
# http://www.baidu.com
# https://org.baidu.net
# https://www.sina.com.cn
print(re.search('^https?://\w+(\.\w+){2,3}$', "http://www.baidu.com"))
print(re.search('^http(|s)://(www|org)\.\w+\.(com|net|\.cn)$', "https://org.baidu.net"))
print(re.search('^http(|s)://(www|org)\.\w+\.(com|net|com\.cn)$', "https://www.sina.com.cn"))

# 2,匹配下列url网址
# https://www.baidu.com/index.html
# https://www.baidu.com:8080/aaa/bbb/index.asp
# https://www.baidu.com:80/ccc/ddd/login.html
print(re.search('^https?://\w+(\.\w+){2,3}(:\d{2,5})?(\w+)*/\w+\.\w+$', "https://www.baidu.com/index.html"))
print(re.search('^https://www\.baidu\.com((:\w+)+|(/\w+)+)+\.(asp|html)$', "https://www.baidu.com:8080/aaa/bbb/index.asp"))
print(re.search('^https://www\.baidu\.com((:\w+)+|(/\w+)+)+\.(asp|html)$', "https://www.baidu.com:80/ccc/ddd/login.html"))


import re
# 爬取笔趣阁小说网内容， 使用正则表达式取出所有好看的玄幻小说名字：
#   http://www.xbiquge.la/xuanhuanxiaoshuo/

# 示例代码:
s = '''</div>
<div class="r">
<h2>好看的玄幻小说</h2>
<ul>
<li><span class="s2"><a href="http://www.xbiquge.la/15/15409/">牧神记</a></span><span class="s5">宅猪</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/0/951/">伏天氏</a></span><span class="s5">净无痕</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/7/7931/">终极斗罗</a></span><span class="s5">唐家三少</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/14/14930/">元尊</a></span><span class="s5">天蚕土豆</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/29/29056/">仙武帝尊</a></span><span class="s5">六界三道</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/2/2210/">全职法师</a></span><span class="s5">乱</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/26/26874/">沧元图</a></span><span class="s5">我吃西红柿</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/13/13959/">圣墟</a></span><span class="s5">辰东</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/10/10512/">人皇纪</a></span><span class="s5">皇甫奇</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/0/10/">武炼巅峰</a></span><span class="s5">莫默</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/0/16/">上古强身术</a></span><span class="s5">我是多余人</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/14/14831/">飞剑问道</a></span><span class="s5">我吃西红柿</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/0/69/">帝霸</a></span><span class="s5">厌笔萧生</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/26/26519/">都市极品医神</a></span><span class="s5">风会笑</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/7/7877/">斗破苍穹</a></span><span class="s5">天蚕土豆</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/0/381/">天域苍穹</a></span><span class="s5">风凌天下</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/0/743/">诡秘之主</a></span><span class="s5">爱潜水的乌贼</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/2/2208/">霸皇纪</a></span><span class="s5">踏雪真人</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/1/1710/">斗罗大陆</a></span><span class="s5">唐家三少</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/27/27256/">临渊行</a></span><span class="s5">宅猪</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/32/32626/">叶辰孙怡夏若雪</a></span><span class="s5">全文免费阅读</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/0/119/">儒道至圣</a></span><span class="s5">永恒之火</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/2/2699/">妖神记</a></span><span class="s5">发飙的蜗牛</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/4/4714/">无敌剑域</a></span><span class="s5">青鸾峰上</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/14/14591/">斗罗大陆4终极斗罗</a></span><span class="s5">唐家三少</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/15/15499/">万道剑尊</a></span><span class="s5">打死都要钱</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/11/11621/">开天录</a></span><span class="s5">血红</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/3/3459/">雪鹰领主</a></span><span class="s5">我吃西红柿</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/11/11559/">太初</a></span><span class="s5">高楼大厦</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/21/21223/">召唤梦魇</a></span><span class="s5">滚开</span></li>
</ul>
<div class="page_b page_b2">喜欢就收藏我们</div>
</div>
'''

# pattern = '<span class="s2"><a.*?">(.*?)</a>'
# list1 = re.findall(pattern, s, re.S)
# print(list1)

import requests
# 当当网图书, 使用正则表达式取出书籍标题，价格，图片路径：
#    http://category.dangdang.com/pg1-cp01.01.02.00.00.00.html
url = 'http://category.dangdang.com/pg1-cp01.01.02.00.00.00.html'
res = requests.get(url)
content = res.text


# 正则解析
# 1. 先获取ul中的内容(所有li,所有的图书
# print(re.findall('^<img data-original=\'(.*?)\' src=.*? alt=.*?>$', a))
list1 = re.findall('<ul class="bigimg" id="component_59">(.*?)</ul>', content, re.S)
content2 = list1[0]
list2 = re.findall('<li.*?(.*?)</li>', content2, re.S)
print(len(list2))
for i, li in enumerate(list2):
    # 图片路径
    img = re.findall('<img.*?=\'(.*?jpg)\'.*?>', li, re.S)[0]
    print(img)


# print(re.findall('target="_blank" ><img .*?=\'(.*?jpg)\'.*?><p class=', content, re.S))
# print(re.findall('target="_blank" ><img .*?alt=\' (.*?)\'.*?/><p class=', content, re.S))
# print(re.findall('<span class="search_now_price">&yen;(.*?)</span>', content, re.S))