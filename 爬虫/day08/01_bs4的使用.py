# 1,导入BeautigulSoup
from bs4 import BeautifulSoup

html = """

<html><head><title>The Dormouse's story</title></head>

<body>

<p class="title" name="dromouse"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were

<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,

<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and

<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;

and they lived at the bottom of a well.

<span><a href="">11111</a>;
</span>

</p>



<p class="story">...</p>

<span class="title">aaaa</span>

"""

#创建 Beautiful Soup 对象

# 使用lxml来进行解析, 把不标准的文档解析为标准的文档
soup = BeautifulSoup(html, "lxml")

# prettify的结果是解析之后的文档结构
# print(soup.prettify())


# 1, 查找第一个p元素
# con = soup.p
# print(con)

# 2, 查找第一个a标签
# con = soup.find("a")
# print(con)

# 3, 查找 id = 'link2' 的a标签
# con = soup.find("a", id='link2')
# print(con)

# 4,查找 class = 'story' 的p标签
# con = soup.find('p', class_="story")
# con = soup.find('p', attrs={'class': 'story'})
# print(con)


# # 5, 查找所有的a标签
# con = soup.find_all('a')
# print(con)

# 6,查找title标签和p标签
# con = soup.find_all(['title', 'b'])
# print(con)

# 7,查找前两个a标签
# con = soup.find_all('a', limit=2)
# print(con)

# 8,查找 class='story'的 p标签
# con = soup.find_all('p', class_='story')
# print(con)

# select方法
# 9,查找 a 标签
# con = soup.select('a')
# print(con)

# 10, 查找class = 'title'的标签
# con = soup.select('p.title')
# print(con)

# 11, 找id = 'link1'的a标签
# con = soup.select('a#link1')
# print(con)

# 12,查找含有name属性的p标签
con = soup.select('p[name="dromouse"]')
print(con)

# 13,查找class='title'的p标签
# con = soup.select('p[class="title"]')
# print(con)

# 14,查找 class="story"的p元素下面所有的a标签
# con = soup.select('p a')
# print(con)

# 15, 查找 class='story'的 p元素下面一级的a标签
# con = soup.select('p > a')
# print(con)

# 16,查找b元素和span元素
# con = soup.select('b, span')
# print(con)

# 17, 找到class="sister"的第一个元素下面的子节点
# con = soup.select('.sister')[0].contents
# con = soup.select('.sister')[0].children
# print(con)

# 18, 获取b标签中的文本
# con = soup.select('b')
# print(con[0].string)
# print(con[0].text)
# print(con[0].get_text())

# 19,查找class='story'的p元素下面的文本
# con = soup.select('.story')
# print(con[0].string)
# print(con[0].text)
# print(con[0].get_text())

# 20,找到第一个a标签的所有属性
# con = soup.select('a')
# print(con[0].attrs)
# print(con[0].attrs.get('id'))
# print(con[0].get('id'))
# print(con[0]['id'])

# 21, 查找class='title' 元素的标签名称
# con = soup.select('.title')
# print(con[0].name)




# class A:
#     def __str__(self):
#         return 'this is a'
#
# a = A()
# print(a)