import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 2, 指定下载的chromedriver的路径
chrome_path = r'D:\chromedriver\chromedriver.exe'

# 3, 初始化driver
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=')

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[1]/div[6]/div[2]/div/div/div[1]/span[1]/a'))

)

obj = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[6]/div[2]/div/div/div[1]/span[1]/a')

obj.click()