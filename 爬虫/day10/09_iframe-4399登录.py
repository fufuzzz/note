import time

from selenium import webdriver

chrome_path = r'D:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)


driver.implicitly_wait(5)

driver.get('http://www.4399.com/')


btn = driver.find_element_by_id('login_tologin')
btn.click()


driver.switch_to.frame('popup_login_frame')


driver.find_element_by_id('username').send_keys('15013518752')
driver.find_element_by_id('j-password').send_keys('python123')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_form"]/fieldset/div[5]/input').click()

driver.switch_to.default_content()

# obj = driver.find_element_by_xpath('//*[@id="loginDiv"]/span')
# obj.click()