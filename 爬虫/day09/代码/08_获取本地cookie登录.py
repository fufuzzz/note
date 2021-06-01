import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

from selenium import webdriver

# 2, 指定下载的chromedriver的路径
chrome_path = r'D:\chromedriver\chromedriver.exe'

# 3, 初始化driver
driver = webdriver.Chrome(executable_path=chrome_path)

# 在添加cookie之前,先去访问网站的任意的一个连接,告诉driver
# 把这个cookie添加到哪个网站上面
driver.get('https://cn.hoyoyo.com/member~login.html')

# 获取本地cookie加入到driver的请求头中, 然后去访问我的账号页面
# 如果能够访问成功, 表示已经成功登录, 如果不成功,表示没有登陆

cookies = 'PHPSESSID=fiks4jlo15hnqn0ored762mtu1; _gcl_au=1.1.511177222.1616051796; _ga=GA1.2.655925126.1616051796; _gid=GA1.2.1618487359.1616051796; _gat=1; ph_portal_c_local_language=zh-cn'

cookies_list = cookies.split(';')


for cookie in cookies_list:
    cookie_data = cookie.split('=')
    print(cookie_data)
    driver.add_cookie({'name': cookie_data[0].strip(), 'value': cookie_data[1].strip()})

driver.get('https://cn.hoyoyo.com/member~login.html')