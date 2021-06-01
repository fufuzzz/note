from selenium import webdriver
import time
import pymysql
import re
import threading
import queue
import multiprocessing
from multiprocessing import Process,Manager,Queue

url_queue = multiprocessing.Queue()
data_queue = multiprocessing.Queue()
t_list = []
t2_list = []


def get_url(j):
    chrome_path = r'D:\chromedriver\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.get(
        f'https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,{j}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=')
    driver.implicitly_wait(5)
    objs = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div/a')
    get_data(objs, driver)


def get_data(objs, driver):
    for i in range(len(objs)):
        # 1, 打开新的tab页
        objs[i].click()
        # driver.execute_script(f"window.open('{objs[1]}')")
        # 2, 切换到新的tab页面
        driver.switch_to.window(driver.window_handles[1])
        # 3,定位到第二个tab页后, 就可以获取源码的内容
        try:
            job_name = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/h1').text
            company = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[1]/a[1]').get_attribute(
                'title')
            location = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[2]/div/p').text.replace('\n', '')
            year = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]').text
            year = year.split('|')[1].strip()
            information = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div').text.replace(' ', '')
            information = re.sub('\n{2,}', '', information)
            information = re.sub('微信分享', '', information)
            # save_51job(job_name, company, location, year, information)
            # print(f'{job_name}, {company}, {location}, {year}, {information}')
            # data_queue.put((job_name, company, location, year, information))
            # print(data_queue.get())
            save_51job(job_name, company, location, year, information)
        except:
            pass
        # 4,关闭页面
        driver.close()
        # 5,切换回第一个tab页面
        driver.switch_to.window(driver.window_handles[0])


def save_51job(job_name, company, location, year, information):
    db = pymysql.connect(user='root', passwd='201314', database='51job')
    # print(job_name, company, location, year, information)
    try:
        with db.cursor() as cur:
            sql = 'insert into job values ("%s", "%s", "%s", "%s", "%s")' % (job_name, company, location, year, information)
            cur.execute(sql)
            db.commit()
    except:
        db.rollback()
    finally:
        db.close()
#

m_list = []
if __name__ == '__main__':

    for j in range(1, 6):
        m = multiprocessing.Process(target=get_url, args=(j, ))
        m.start()
    for m in m_list:
        m.join()

















    # for i in range(3):
    #     t = threading.Thread(target=get_data)
    #     t2 = threading.Thread(target=save_51job)
    #     t.start()
    #     t2.start()
    #     t_list.append(t)
    #     t2_list.append(t2)
    #
    # for o, p in zip(t_list, t2_list):
    #     o.join()
    #     p.join()
