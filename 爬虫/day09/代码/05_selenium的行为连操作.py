# 1, 导包
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

from selenium import webdriver

# 2, 指定下载的chromedriver的路径
chrome_path = r'D:\chromedriver\chromedriver.exe'

# 3, 初始化driver
driver = webdriver.Chrome(executable_path=chrome_path)

# 4, 请求网页
driver.get('https://www.baidu.com')
# driver.get('https://kyfw.12306.cn/otn/regist/init')

# 定位百度的输入框
inputTag = driver.find_element_by_id('kw')
# 定位到百度一下按钮
submitTag = driver.find_element_by_id('su')

# 创建一个行为链对象
actions = ActionChains(driver)
# 把鼠标移动到输入框
actions.move_to_element(inputTag)
# 发送数据到输入框
actions.send_keys_to_element(inputTag,'python')
# 把鼠标移动到百度一下按钮对象上
actions.move_to_element(submitTag)
# 点击百度一下
actions.click(submitTag)
# 执行所有的行为
actions.perform()

# 还有更多的鼠标相关的操作。
#
# click_and_hold(element)：点击但不松开鼠标。
#
# context_click(element)：右键点击。
#
# double_click(element)：双击。
#
# 更多方法请参考：http://selenium-python.readthedocs.io/api.html