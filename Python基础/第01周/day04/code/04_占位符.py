
# 占位符

# %s 字符串
# %d 整数
# %f 小数

name = '渣渣辉'
age = 60
height = 1.8

print("大家好,我是渣渣辉,我今年60,身高1.8m")
print("大家好,我是%s,我今年%d,身高%fm" % (name, age, height))
print("大家好,我是%s,我今年%d,身高%.2fm" % (name, age, height))  # 保留两位小数


# .format()
print("大家好,我是{},我今年{},身高{}m".format(name, age, height))
print("大家好,我是{a},我今年{b},身高{c}m".format(a=name, b=age, c=height))

# f-string 推荐
print(f"大家好,我是{name},我今年{age},身高{height}m")

