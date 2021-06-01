# 1, 导入urllib中的request 包
from urllib import request

# 2, 下载图片(网络图片地址,本地保存的地址)
request.urlretrieve(url='https://www.baidu.com/img/PCpad_012830ebaa7e4379ce9a9ed1b71f7507.png', filename='bd.png')