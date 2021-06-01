from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_path = r'D:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=')
driver.implicitly_wait(5)
data = []
num = 1
# url = driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[6]/div/div/div/div[1]/span[1]/a')
# print([obj.get_attribute('href') for obj in url])
while num < 100:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@id="content"]/div/div[1]/div[6]/div[{num}]/div/div/div[1]/span[@class="rank-num"]'))
    )
    num = driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[6]/div/div/div/div[1]/span[@class="rank-num"]')[-1].text
    num = int(num)
    driver.execute_script('window.scrollBy(100, 2000)')
    urls = driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[6]/div/div/div/div[1]/span[1]/a')
    urls = [obj.get_attribute('href') for obj in urls]
    names = driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[6]/div/div/div/div[1]/span[1]/a')
    names = [obj.text for obj in names]
    scores = driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[6]/div/div/div/div[4]/span[2]')
    scores = [obj.text for obj in scores]


    for name, url, score in zip(names, urls, scores,):
        data.append({
            'name':  name,
            'url': url,
            'score': score
        })

print(data)