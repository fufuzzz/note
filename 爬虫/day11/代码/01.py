import time
from selenium import webdriver


chrome_path = r'D:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx')

driver.find_element_by_id('email').send_keys('290793992zb@163.com')
time.sleep(1)
driver.find_element_by_id('pwd').send_keys('python123')

# 定位到验证码对象,进行截图
driver.find_element_by_id('imgCode').screenshot('./code.jpg')

# 通过第三方api识别验证码
code = get_code()

driver.find_element_by_id('code').send_keys(code)

# 点击登录
driver.find_element_by_id('denglu').click()