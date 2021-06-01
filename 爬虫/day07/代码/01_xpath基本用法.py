# 1,导入etree包
from lxml import etree
#
s = '''
    <div>

    <ul>

         <li class="item-0"><a href="link1.html">first item</a><>

         <li class="item-1" id="w"><a href="link2.html">second item</a><>

         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a><>

         <li class="item-1" id="abc"><a href="link4.html">fourth item</a><>

         <li class="item-0" id="w"><a href="link5.html">fifth item</a><>

    </ul>
    <span>123456</span> 
    
 </div>


'''


# 2, 把获取的原码放入 etree.HTML 方法中分析
html = etree.HTML(s)


# 如果是一个html的代码片段, 那么etree.HTML会把代码片段补充完整,会在代码片段前后加入html和body
# 查看xpath的对象的html的内容,用到的方法是etree.tostring()
# print(etree.tostring(html))

# / 是获取当前文件的直接子节点
# 通过xpath返回的结果是一个列表, 列表中找到是元素对象
# con = html.xpath('/html')
# print(etree.tostring(con[0]))

# 2, 找当前文档的所有li标签
# con = html.xpath('//li')
# for c in con:
#     print(etree.tostring(c))

# 3, ./表示查找当前元素的直接子元素
# ul = html.xpath('//ul')

# 每个xpath语法返回的对象可以继续使用xpath语法进行分析
# li = ul[0].xpath('./li')
# li = ul[0].xpath('..//li')
# print(li)


# 怎么获取一个对象是实例化的哪个类
# print(type(ul[0]))
from lxml.etree import _Element

# 4,找含有id属性的li标签
# con = html.xpath('//li[@id]')
# print(con)

# 5, 查找li标签的class属性=item-inactive的li属性
# con = html.xpath('//li[@class="item-inactive"]')
# print(con)

# 6, 查找 class="item-1" 的li元素,并且获取li元素中id属性的值
# con = html.xpath('//li[@class="item-1"]/@id')
# print(con)

# 7, 查找 class="item-1" 并且 id = "w" 的li元素
# con = html.xpath('//li[@class="item-1" and @ id="w"]')
# con = html.xpath('//li[@class="item-1" or @ id="w"]')
# for i in con:
#     print(etree.tostring(i))

# 8, 查找不含有id属性的li标签
# con = html.xpath('//li[not(@id="w")]')
# for i in con:
#     print(etree.tostring(i))


# 9,查找a标签和span标签
# con = html.xpath('//a | //span')
# for i in con:
#     print(etree.tostring(i))

# 10, 查找li元素的class属性包含1
# con = html.xpath('//li[contains(@class,"1")]')
# for i in con:
#     print(etree.tostring(i))

# 11, 查找li元素id以"a"开头的li
# con = html.xpath('//li[starts-with(@id, "a")]')
# for i in con:
    # print(etree.tostring(i))

# 12, 查找最后一个li元素
# con = html.xpath('//ul/li[last()]')
# for i in con:
#     print(etree.tostring(i))


# 13,查找ul下面第一个li元素
# con = html.xpath('//ul/li[position()=1]')
# con = html.xpath('//ul/li[1]')
# for i in con:
#     print(etree.tostring(i))

# 14, 查找第3个li标签后面的所有元素
# con = html.xpath('//ul/li[position()>3]')
# for i in con:
#     print(etree.tostring(i))

# 15, 查找第二个 a 标签 下面的文本
# con = html.xpath('//a[@href="link2.html"]/text()')
# con = html.xpath('//ul/li[2]//text()')
# print(con)
# for i in con:
#     print(etree.tostring(i))