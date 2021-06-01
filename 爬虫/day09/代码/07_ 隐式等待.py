import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

from selenium import webdriver

# 2, 指定下载的chromedriver的路径
chrome_path = r'D:\chromedriver\chromedriver.exe'

# 3, 初始化driver
driver = webdriver.Chrome(executable_path=chrome_path)

# 设置隐式等待的超时时间  针对所有元素
driver.implicitly_wait(5)

driver.get('https://www.baidu.com')

driver.find_element_by_id('su')
