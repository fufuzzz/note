# 爬取百度搜索python关键字的页面内容

# 1, 导入requests包
import requests

# 模拟正常浏览器发送请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}

data = {
    'wd': 'java'
}

# 2,用get方法请求百度的页面
req = requests.get(url='https://www.baidu.com/s?wd=python', headers=headers)
req2 = requests.get(url='https://www.baidu.com/s?wd=python', params=data, headers=headers)

# 3,获取爬取网页的内容
# print(req.text)

# 返回的源代码的字节形式
# print(req.content)
# print(req.content.decode())


# 返回网页的编码格式
print(req.encoding)
req.encoding = 'utf-8'

# 返回网页状态码
# 返回403,表示当前用户没有权限
print(req.status_code)

# 获取json数据
# print(req.json())

# 获取请求头信息
print(req.request.headers)


# 获取请求的url
print(req.url)

# 4,把爬取的文件保存到文件
# with open('baidu.html', 'w', encoding='utf-8') as fp:
#     fp.write(req.text)

#
# with open('baidu.html', 'wb') as fp:
#     fp.write(req.content)
#
# with open('java.html', 'wb') as fp:
#     fp.write(req.content)