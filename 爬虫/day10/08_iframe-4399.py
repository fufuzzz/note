import time

from selenium import webdriver

chrome_path = r'D:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

# 隐式加载,只针对当前的页面,对iframe中的页面没有任何效果的
driver.implicitly_wait(5)

driver.get('http://www.4399.com/')

# 1, 找到注册链接,再点击
btn = driver.find_element_by_id('login_toregister')
btn.click()

# 2, 由于用户名的input框是在iframe页面中的,
#  所以必须有当前页面切换到iframe的页面中
#  frame参数就是iframe标签中name属性的值
driver.switch_to.frame('popup_reg_frame')

# 3, 定位到弹出框的用户名input, 填写数据
driver.find_element_by_id('j-username').send_keys('123456')
time.sleep(2)

# 4, 点击关闭按钮
# 由于关闭按钮的对象不在iframe的页面中,他是在最外层
# 所以要切换到万层页面
driver.switch_to.default_content()

obj = driver.find_element_by_xpath('//*[@id="loginDiv"]/span')
obj.click()