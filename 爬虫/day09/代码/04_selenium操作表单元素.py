# 1, 导包
import time
from selenium.webdriver.support.ui import Select

from selenium import webdriver

# 2, 指定下载的chromedriver的路径
chrome_path = r'D:\chromedriver\chromedriver.exe'

# 3, 初始化driver
driver = webdriver.Chrome(executable_path=chrome_path)

# 4, 请求网页
# driver.get('https://www.baidu.com')
driver.get('https://kyfw.12306.cn/otn/regist/init')

# 1, 定位百度的搜索框,输入文字python
# obj = driver.find_element_by_id('kw')
# obj.send_keys('python')
# time.sleep(2)
# inputTag.clear()

# 2, 定位百度一下按钮,发送点击事件
# btn = driver.find_element_by_id('su')
# btn.click()

# 3,百度注册页面, 接受妥协的复选框点击事件
# obj = driver.find_element_by_id('')


# 4,根据索引定位select的选项
obj = driver.find_element_by_id('cardType')
ele = Select(obj)
# ele.select_by_index(1)

# 根据值定位
# ele.select_by_value("B")

# 根据
ele.select_by_visible_text("台湾居民来往大陆通行证")
