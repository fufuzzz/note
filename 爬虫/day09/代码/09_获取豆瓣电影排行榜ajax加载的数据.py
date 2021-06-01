import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium import webdriver

# 2, 指定下载的chromedriver的路径
chrome_path = r'D:\chromedriver\chromedriver.exe'

# 3, 初始化driver
driver = webdriver.Chrome(executable_path=chrome_path)

# 隐式等待针对所有的对象
driver.implicitly_wait(3)

# driver能够获取ajax显示在浏览器的源代码
driver.get('https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=')

# 获取drver源码的方式,
# page_source 能够获取ajax加载的数据
# 前提必须是,ajax数据已经加载到页面上
# print(driver.page_source)

driver.find_element_by_class_name('movie-content')

print(driver.page_source)
