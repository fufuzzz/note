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
