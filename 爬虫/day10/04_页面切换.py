from selenium import webdriver
import time

chrome_path = r'D:\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://www.baidu.com/')

time.sleep(2)

# driver.get('https://www.chinaz.com/')

# execute_script 方法是用来执行js的语法, 用引号把js语句包起来
# driver.execute_script("alert('hello world')")
# window.open()是js语法, 作用是在新的tap页中打开一个网站
# 参数就是打开的网址
driver.execute_script("window.open('https://www.chinaz.com/')")

# current_url 表示driver的当前页面
# print(driver.current_url)
# obj = driver.find_element_by_id('kw')
# print(obj)

# 如果想要获取第二个tab页中的元素对象,那么必须从第一个tab页面切换到第二个tab页面
# 切换页面的方法是 driver.switch_to.Window(), 参数就是第一个tab页面
# 参数的表示方法是driver.window_handles, 这个属性是一个列表, 每个值就是不同的tab对象
# tab的对象 下标从0开始
# 例如 driver.window_handles[0] 表示第一个tab对象, driver.window_handles[1] 表示第二个对象
driver.switch_to.window(driver.window_handles[1])

# 新打开chinaz.com之后,从源代码中获取 class="header-logo"的div对象
# obj = driver.find_element_by_class_name('header-logo')
# print(obj)
time.sleep(2)
# 关闭第二个tab页, 然后在第一个tab页中找百度一下这个按钮对象
driver.close()
# 虽然关闭了第二个tab页面,但是driver 还停留在这个页面
# 所以若果要去第一个tab页面中获取数据, 必须切换回第一个tab页
driver.switch_to.window(driver.window_handles[0])

# print(driver.current_url)
obj = driver.find_element_by_id('su')

print(obj)