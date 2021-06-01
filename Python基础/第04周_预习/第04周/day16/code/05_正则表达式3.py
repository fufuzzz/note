
# 匹配字符数量

import re

# ? : 表示前面字符出现的次数为0次或1次, 非贪婪模式
# + : 表示前面字符出现的次数为1次或多次, 贪婪模式(会尽力匹配)
# * : 表示前面字符出现的次数为0次或多次, 贪婪模式
# {}: 表示前面字符出现的次数可以自定义, 贪婪模式
#   {3} : 刚好为3次
#   {3,5}: 3次-5次
#   {3,}: 至少三次(3次或以上)
#   {,5}: 最多5次

# ?: 表示前面字符出现的次数为0次或1次
print(re.search('ora?nge', 'orange'))
print(re.search('123(orange)?', '123orange'))

# + : 表示前面字符出现的次数为1次或多次
print(re.search('ora+nge', 'orange'))
print(re.search('123(orange+)+', '123orange'))

# * : 表示前面字符出现的次数为0次或多次
print(re.search('ora*nge', 'orange'))
print(re.search('123(orange)*', '123orangeorange'))

# {}: 表示前面字符出现的次数可以自定义, 贪婪模式
print(re.search('ora{3}nge', 'oraaaange'))
print(re.search('ora{3,5}nge', 'oraaaange'))
print(re.search('ora{3,}nge', 'oraaaaaaaaaaaaaange'))
print(re.search('ora{,5}nge', '123oraaaaange'))

# 单个字符 和 字符数量使用
print(re.search('banana is .*', 'banana is ,,,,'))
print(re.search('banana is .\w+', 'banana is nice'))
print(re.search('banana price is .\d+', 'banana price is 998.'))

s = '''<div class="weather_li_open" style="width:555px;">
          <p>
            <a href="http://www.weather.com.cn/alarm/">预警</a>
            <a href="http://typhoon.weather.com.cn/" target="_blank">台风路径</a>
            <a href="http://www.weather.com.cn/space/">空间天气</a>
            <a href="http://p.weather.com.cn/">图片</a>
            <a href="http://video.weather.com.cn/">视频</a>
            <a href="http://www.weather.com.cn/zt/">专题</a>
            <a href="http://www.weather.com.cn/air/">环境</a>
            <a href="http://www.weather.com.cn/trip/">旅游</a>
            <a href="http://www.sportsweather.cn/golf/">高尔夫</a>
            <a href="http://www.weather.com.cn/forecast/skiweather.shtml">滑雪</a>
            <a href="http://www.weather.com.cn/aviation/">航空</a>
            <a href="http://www.weather.com.cn/beltroad/">一带一路</a>
          </p>
          <p style="border:none;" class="erp">
            <a href="http://www.weather.com.cn/tqbx/">保险</a>
            <a href="http://www.weather.com.cn/slpd/index.shtml">水利</a>
            <a href="http://www.weather.com.cn/agriculture/pest/">农业·病虫害</a>           
            <a  href="http://www.weather.com.cn/science/">科普</a>
            <a href="http://www.weather.com.cn/fzjz/">减灾</a>
            <a href="http://www.weather.com.cn/climate/">生态</a>
            <!-- <a href="http://marketing.weather.com.cn/">商业合作</a> -->
            <a href="https://cj.weather.com.cn/">天气插件</a>
            <a href="http://www.weather.com.cn/province/">省级站</a>
          </p>
        </div>'''
# .*?:匹配到最近的
# res = re.findall('<p(.x*?)</p>', s, re.S)
# print(res)
# print(len(res))
print(re.S)
res = re.findall('<a.*?>(.*?)</a>', s, re.S)
print(res)
