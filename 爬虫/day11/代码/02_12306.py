from selenium import webdriver

# 创建options对象
# options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=http://117.95.214.222:4236')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_path = r'D:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://kyfw.12306.cn/otn/resources/login.html')

# 把本地成功登录的cookie加入到driver的头中
cookie = ''
cookie_list = cookie.split(';')
for obj in cookie_list:
    c = obj.split('=')
    driver.add_cookie({'name': c[0].strip(), 'value': c[1].strip()})

# 3, 访问购买单程票的页面
driver.get('')

# 4,关闭弹框
driver.find_element_by_id('').click()

# 5,定位到出发地, 自动写入"深圳", 点击出现的第一个
d1 = driver.find_element_by_id('')
d1.click()
d1.send_kyes('深圳')
driver.find_element_by_id('').click()

# 6,定位到目的地, 自动写入"北京", 点击出现的第一个
d1 = driver.find_element_by_id('')
d1.click()
d1.send_kyes('武汉')
driver.find_element_by_id('').click()

# 7,定位到 出发日对象, 选择28号, 点击
btn = driver.find_element_by_id('train_date')
btn.click()
driver.find_element_by_xpath('')
falg = True
while falg:
# 8,点击查询按钮
    driver.find_element_by_id('query_ticket').click()

    # 9, 逻辑, 先找一个二等有票的, 把整个自动订票的逻辑跑通
    # 然后在定位到一个候补的车次,不断的循环点击查询按钮,直到候补变成有票或者是一个数字的
    # 先找G72的二等座

    # 10, 通过显示等待,等待id是queryLeftTable 的tbody元素下面所有的tr加载出来
    WebDriverWait.until(
        EC.presence_of_all_elements_located((By.XPATH, ''))
    )

    trs = driver.find_element_by_xpath('')

    # 11,循环找tr下面第一个td标签下面的车次是G72
    for tr in trs:
        con = tr.find_element_by_xpath('').text
        if con == 'G72':
            # 12,判断tr下面的第四个td元素的文本
            # 如果是文本有或者十一数字, name就点击最后一个单元格的预订按钮
            edz = tr.find_element_by_xpath('').text
            if edz == '有' or edz.isdigint():
                tr.find_element_by_xpath('').click()
                flag = False
                break

# 12, 等待页面的跳转 选择乘车人信息的页面
WebDriverWait(driver, 10).until(
    EC.url_to_be('')
)

# 13,请选择乘车人, 点击提交按钮
driver.find_element_by_id('').click()
driver.find_element_by_id('').click()

# 14,再弹出的页面中 点击 确认按钮
driver.find_element_by_id().click()