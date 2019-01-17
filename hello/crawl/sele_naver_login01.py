import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drvPath = 'C:\chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome('C:\chromedriver_win32/chromedriver.exe')
UserId = {"1":"la"}  # "2":"rr", "3":"y", "4":"b", "5":"a", "6":"ck"}
UserPw = {"7":"ka94*76058113"}          #{"7":"ka", "8":"94*", "9":"76", "10":"05", "11":"81", "12":"13"}

UserId1 = {"2":"rr"}
UserPw1 = ""

UserId2 = {"3":"y"}
UserPw2 = ""

UserId3 = {"4":"b"}
UserPw3 = ""

UserId4 = {"5":"a"}
UserPw4 = ""


UserId5 = {"6":"ck"}
UserPw5 = {"7":"ka94*76058113"} 



driver.get("https://www.naver.com")
time.sleep(1)

driver.find_element_by_class_name('lg_local_btn').click()
print("click big button!!")
time.sleep(1)

id = driver.find_element_by_id('id')
for i in UserId:
    time.sleep( random.randrange(1, 5) / 10 )
    id.send_keys(i["1"])


id.send_keys(Keys.TAB)
time.sleep(1)


pw = driver.find_element_by_id('pw')
for i in UserPw:
     time.sleep(random.randrange(1, 5) / 10)
     pw.send_keys(i)

time.sleep(1)
  
id = driver.find_element_by_id('id')
for i in UserId1:
    time.sleep( random.randrange(1, 5) / 10 )
    id.send_keys(i["2"])


id.send_keys(Keys.TAB)
time.sleep(1)


pw = driver.find_element_by_id('pw')
for i in UserPw1:
     time.sleep(random.randrange(1, 5) / 10)
     pw.send_keys(i)

time.sleep(1)

id = driver.find_element_by_id('id')
for i in UserId2:
    time.sleep( random.randrange(1, 5) / 10 )
    id.send_keys(i["3"])


id.send_keys(Keys.TAB)
time.sleep(1)


pw = driver.find_element_by_id('pw')
for i in UserPw2:
     time.sleep(random.randrange(1, 5) / 10)
     pw.send_keys(i)

time.sleep(1)   

id = driver.find_element_by_id('id')
for i in UserId3:
    time.sleep( random.randrange(1, 5) / 10 )
    id.send_keys(i["4"])


#id.send_keys(Keys.TAB)
#time.sleep(1)


pw = driver.find_element_by_id('pw')
for i in UserPw3:
     time.sleep(random.randrange(1, 5) / 10)
     pw.send_keys(i)

time.sleep(1)     

id = driver.find_element_by_id('id')
for i in UserId4:
    time.sleep( random.randrange(1, 5) / 10 )
    id.send_keys(i["5"])


#id.send_keys(Keys.TAB)
#time.sleep(1)


pw = driver.find_element_by_id('pw')
for i in UserPw4:
     time.sleep(random.randrange(1, 5) / 10)
     pw.send_keys(i)


id = driver.find_element_by_id('id')
for i in UserId5:
    time.sleep( random.randrange(1, 5) / 10 )
    id.send_keys(i["6"])


#id.send_keys(Keys.TAB)
#time.sleep(1)


pw = driver.find_element_by_id('pw')
for i in UserPw5:
     time.sleep(random.randrange(1, 5) / 10)
     pw.send_keys(i["7"])

time.sleep(1)



#pw = driver.find_element_by_id('pw')
#for i in UserPw:
#     time.sleep(random.randrange(1, 5) / 10)
#     pw.send_keys(i)


time.sleep(0.5)
pw.send_keys(Keys.RETURN)

time.sleep(1)


time.sleep(5)                # cf.  driver.implicitly_wait(5)
#driver.quit() # driver.close()