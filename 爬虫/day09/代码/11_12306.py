from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 2, 指定下载的chromedriver的路径
chrome_path = r'D:\chromedriver\chromedriver.exe'

# 代理设置
# 创建driver的选项对象
options = webdriver.ChromeOptions()
# 在选项中设置代理ip
options.add_argument('--proxy-server=http://117.86.27.111:4264')

# 3, 初始化driver
driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)


# 4,手动登录
driver.get('https://kyfw.12306.cn/otn/resources/login.html')

# 通过显式等待, 等待用户成功登录后
# 判断只要当前页面的地址是 https://kyfw.12306.cn/otn/view/login.html
# 那就表面用户已经成功登录
WebDriverWait(driver, 100).until(
    EC.url_to_be('https://kyfw.12306.cn/otn/view/login.html')

)


# 5, 登录成功之后,跳转到单程页面去购票
driver.get('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc')

