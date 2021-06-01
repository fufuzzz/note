# 1.判断下面标识符是否合法并说明不合法的原因
# @abc.com   =>不合法,@和.不合法
# 123ok      =>不合法,不能以数字开头
# _xiaoming  =>合法
# xiaoming_$ =>不合法,$不能
# interface  =>合法
# sina@163   =>不合法,@不能


# 2.从控制台输入圆的半径.计算周长和面基,π=3.14

r = float(input("请输入半径:"))
print("圆的周长是:", 2*r*3.14, sep='')
print("圆的面基是:", r**2*3.14)

# 3.一辆汽车以40km/h的速度行驶,行驶了45678.9km,求所用的时间

t = 45678.9/40
print("所用的时间是:", t)

# 4.华氏温度转摄氏温度
# 【提示: 将华氏温度转换为摄氏温度(F是华氏温度)  F = 1.8C + 32】

F = float(input("请输入一个华氏温度:"))
C = (F-32)/1.8
print("转换为摄氏温度是:", C)

# 5.入职薪水10K,每年涨幅入职薪水的5%,50年后工资多少?

wages = 10*(1+0.05*50)
print("50年后的工资是:", wages)

# 6.为了抵抗洪水,战士连续作战89小时,编程计算共多少天零多少小时?

day = 89 // 24
hour = 89 % 24
print("是", day, "天", hour, "个小时", sep='')

# 7.给定一个5位数,分别把这个数字的万位,千位,百位,十位,个位算出来并显示.如:34567
n = 34567
wanwei = n // 10000
qianwei = n // 1000 % 10
baiwei = n // 100 % 10
shiwei = n // 10 % 10
gewei = n % 10

print("万位:", wanwei)
print("千位:", qianwei)
print("百位:", baiwei)
print("十位:", shiwei)
print("个位:", gewei)


q = 45678
day1 = q // (60*60*24)
hour2 = q // 60*60 % 24
minute = q // 60 % 60
second = q % 60

print("是", day1, "天", hour2, "个小时", minute, "分钟", second, "秒", sep='')
# 8.判断一个年份是否为闰年:
#   判断闰年的条件是:满足以下两个要求的一个即可:
#       1.能被4整除,但是不能被100整除
#       2.能被400整除

year2 = int(input("输入一个年份"))
z = year2 % 4
y = year2 % 100
x = year2 % 400
if (z==0 and y!=0) or x == 0:
    print(True)
else :
    print(False)


