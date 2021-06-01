
import time

# 时间戳: 指定时间距离1970年1月1日0点的秒数
# UTC: 国际标准时间, 格林尼治时间
# 北京: 东八区

# 当前时间的时间戳 timestamp
print(time.time())

# 暂停0.6秒
time.sleep(0.6)


# datetime 模块
import datetime

# 创建日期对象
d = datetime.datetime.now()
# print(d)  # 2021-01-26 10:36:04.653363
# print(type(d))  # <class 'datetime.datetime'>


# 创建指定时间
d = datetime.datetime(year=3000, month=12, day=31, hour=10, minute=10,second=10)
# print(d)

# 日期对象的属性
print(d.year, d.month, d.day)  # 年月日
print(d.hour, d.minute, d.second)  # 时分秒
print(d.date(), d.time())  # 3000-12-31 10:10:10

# 日期对象 => 字符串: strftime
# 字符串 => 日期对象: strptime
# strftime()
print(d.strftime('%Y-%m-%d %H-%M-%S'))  # '3000-12-31 10-10-10'
print(d.strftime('%a %A %b %B'))  # Wed Wednesday Dec December
print(d.strftime('%c'))  # Wed Dec 31 10:10:10 3000
print(d.strftime('%x %X'))  # 12/31/00 10:10:10
print(d.strftime('%Y{}%m{}%d{}').format('年', '月', '日'))

# strptime()
d2 = d.strptime('2022-11-11', '%Y-%m-%d')
print(d2, type(d2))

# 时间戳
# d.timestamp(): 日期对象=>时间戳
print(d.timestamp())  # 32535137410.0
# d.fromtimestamp(32535137410.0): 时间戳 => 日期对象
print(d.fromtimestamp(32535137410.0))

# 时间戳 : 传输
# 日期对象: 代码中用
# 日期字符串: 传输,显示到页面

# 时间差
dt = datetime.timedelta(days=-10, hours=7)
now = datetime.datetime.now()
print(now + dt)
print(now - dt)

# 2个日期相差的时间
d1 = datetime.datetime(2021, 1, 1)
d2 = datetime.datetime(2021, 1, 26)
d3 = d2 - d1
print(d3, type(d3), d3.days)
