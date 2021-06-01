# 1,导入webdriver的包
import time

from selenium import webdriver

# 2,指定下载的chromedriver的路径
chrome_path = r'D:\chromedriver\chromedriver.exe'

# 3,初始化driver
driver = webdriver.Chrome(executable_path=chrome_path)

# 4,请求网页
driver.get('https://www.baidu.com')

# time.sleep(3)
# print(driver.page_source)

# 关闭tab页面
# driver.close()

# 关闭浏览器
# dirver = quit()


# 5,通过id 定位
# btn = driver.find_element_by_id('su')
#
# print(btn.get_attribute('value'))

# 6, 通过class定位并且获取文本
# class_ = driver.find_element_by_class_name('hot-refresh-text')
# print(class_.text)

# 7,截图 整个页面
# driver.save_screenshot('./baidu.png')

# 8,截图 某个特定对象
# btn = driver.find_element_by_id('su')
# btn.screenshot('./btn.png')

# 9,通过name获取对象, name属性是针对 input 框中name的属性
# obj = driver.find_element_by_name('wd')
# print(obj.get_attribute('maxlength'))

# 10, 通过标签名称获取对象
# obj = driver.find_element_by_tag_name('form')
# print(obj.get_attribute('id'))

# 11, 通过xpath获取对象
# 在selenium中xpath语法只能定位到这个对象,而不能定位到文本值和属性值
# obj = driver.find_element_by_xpath('//div[@id="s-top-left"]/a[4]')
# print(obj.text)

# 12, 通过css选择器获取对象
# obj = driver.find_element_by_css_selector('#su')
# print(obj.get_attribute('value'))

# 13, 通过标签名称定位相同标签的多个元素
# obj = driver.find_elements_by_tag_name('a')
# print(obj)

