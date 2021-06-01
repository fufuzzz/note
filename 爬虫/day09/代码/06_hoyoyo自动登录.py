import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

from selenium import webdriver

# 2, 指定下载的chromedriver的路径
chrome_path = r'D:\chromedriver\chromedriver.exe'

# 3, 初始化driver
driver = webdriver.Chrome(executable_path=chrome_path)

# 访问登录页面
driver.get('https://cn.hoyoyo.com/member~login.html')

# 输入用户名和密码, 点击登录
driver.find_element_by_id('email').send_keys('290793992zb@163.com')
time.sleep(1)
driver.find_element_by_id('password').send_keys('python123')
time.sleep(1)
driver.find_element_by_xpath('//button[contains(@class, "btn-success")]').click()