# 一

import re
# s = "asdfjvjadsffvaadfkfasaffdsasdffadsafafsafdadsfaafd"
# res = re.findall(r'(af)', s)
# print(len(res))
# 查找字符串中有多少个af
#
# 二
#
# s = "abDEe23dJfd343dPOddfe4CdD5ccv!23rr"
# res = re.findall(r'[a-z]', s, re.I)
# print(res)

# 取出字符串中的所有字母
#
# 三
#
# s = "zhangsan   lisi  wangwu"
# res = re.findall(r'\b[^\s]+\b',s)
# # res = re.split(r'\s+', s)
# print(res)
# 规则是按照空格出现一次或者多次切割
#
# 四
#
# s = "c:\\abc\\a.txt"
# res = re.split(r'\\', s)
# print(res)
# 用正则\\切割
#
# 五
#
# s = "wer8934605juo123wa89320571f"
# res = re.sub(r'\d{5,}', '#', s)
# print(res)
# 将连续5个以上数字替换成#
#
# 六
#
# s = "cudddbhuuujddd"
# res = re.sub(r'([a-z])\1+', '&', s)
# print(res)

# 将多个重复字母替换成&
#
# 七
#
# s = "min tian jiu yao fang jia le ,da jia"
# res = re.findall(r'\b([a-zA-Z]{3}\b)', s)
# print(res)
# 获取长度为3个字母的单词
#
# 八
#
# s = 'THREE people at HERE do some THING'
# res = re.findall(r'\b[a-z]*?e\b', s, re.I)
# print(res)
# 获取单词结尾是e的单词
#
# 九
#
# s = "我我...我我...我要..要要...要要...学学学...学学...编编编..编程..程.程...程...程"
# res = re.sub(r'\.+', '', s)
# res = re.sub(r'(.)\1+', r'\1', res)
# print(res)

# 修改为‘我要学编程’
# 十
#
s = """

<div>

	<img src='1.png'>

	<img src='2.png'>

</div>

<div>

	<img src='11.png'>

	<img src='22.png'>

</div>

"""
#
# 输出结果为列表
#
# [ "<img src='1.png'><img src='2.png'>" , "<img src='11.png'><img src='22.png'>" ]
res = re.findall(r'<div>(.*?)</div>', s, re.S)
for n in res:
    res = re.sub(r'[\n\t]', '', n)
    print(res)