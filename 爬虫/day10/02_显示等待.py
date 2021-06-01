from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_path = r'D:\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_path)

# driver.implicitly_wait(3)

# driver能够获取ajax显示在浏览器的源代码
driver.get('https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=')

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[1]/div[6]/div[3]/div/div/div[1]/span[1]/a'))
)

obj = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[6]/div[3]/div/div/div[1]/span[1]/a')
obj.click()