
from selenium import webdriver

chrome_path=r'E:\Google\chromedriver\chromedriver.exe'

driver=webdriver.Chrome(executable_path=chrome_path)

driver.implicitly_wait(3)
driver.get('https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=')

objs=driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div/a')[1:]
data_list=[]
for obj in objs:
    obj.click()

    driver.switch_to.window(driver.window_handles[1])
    title=driver.find_element_by_tag_name('h1').text
    print(title)
    company=driver.find_element_by_class_name('cname').find_element_by_tag_name('a').text
    print(company)
    infos=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]').text
    info=infos.split('|')
    year=info[1].strip()
    print(year)
    jobinfos=driver.find_element_by_xpath('//div[@class="bmsg job_msg inbox"]').text
    jobinfo=jobinfos.replace('\n','').replace('\r','')
    print(jobinfo)
    # print(driver.current_url)
    data = {
        'title':title,
        'company':company,
        'year':year,
        'jobinfo':jobinfo
    }
    data_list.append(data)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # break

