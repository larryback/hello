import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drvPath = 'C:\chromedriver_win32 (1)/chromedriver.exe'
driver = webdriver.Chrome('C:\chromedriver_win32 (1)/chromedriver.exe')
UserId = "larryback"
UserPw =  ""

UserId1 = "rr"
UserPw1 = ""

UserId2 = "y"
UserPw2 = ""

UserId3 = "b"
UserPw3 = ""

UserId4 = "a"
UserPw4 = ""


UserId5 = "ck"
UserPw5 = "ka94*76058113"



driver.get("https://www.naver.com")
time.sleep(1)

driver.find_element_by_class_name('lg_local_btn').click()
print("click big button!!")
time.sleep(1)

id = driver.find_element_by_id('id')
#for i in UserId:
#    time.sleep( random.randrange(1, 5) / 10 )
id.send_keys(UserPw)

id.send_keys(Keys.CONTROL, "a")
id.send_keys(Keys.CONTROL, "x")
id.send_keys(Keys.TAB)
time.sleep(1)


pw = driver.find_element_by_id('pw')
pw.send_keys(Keys.CONTROL, "v")
#for i in UserPw:
#     time.sleep(random.randrange(1, 5) / 10)
#     pw.send_keys(i)

time.sleep(1)
  
id = driver.find_element_by_id('id')
id.send_keys(UserId)
id.send_keys(Keys.CONTROL, "a")
id.send_keys(Keys.CONTROL, "x")
id.send_keys(Keys.CONTROL, "v")


#for i in UserId1:
#    time.sleep( random.randrange(1, 5) / 10 )
#    id.send_keys(i)


id.send_keys(Keys.TAB)
time.sleep(1)


#pw = driver.find_element_by_id('pw')
#for i in UserPw1:
#     time.sleep(random.randrange(1, 5) / 10)
#     pw.send_keys(i)

time.sleep(1)

#id = driver.find_element_by_id('id')
#for i in UserId2:
#    time.sleep( random.randrange(1, 5) / 10 )
#    id.send_keys(i)


id.send_keys(Keys.TAB)
time.sleep(1)



#pw = driver.find_element_by_id('pw')
#for i in UserPw2:
#     time.sleep(random.randrange(1, 5) / 10)
#     pw.send_keys(i)

time.sleep(1)   


#id = driver.find_element_by_id('id')
#for i in UserId3:
#    time.sleep( random.randrange(1, 5) / 10 )
#    id.send_keys(i)


#id.send_keys(Keys.TAB)
#time.sleep(1)


#pw = driver.find_element_by_id('pw')
#for i in UserPw3:
#     time.sleep(random.randrange(1, 5) / 10)
#     pw.send_keys(i)

#time.sleep(1)     

#id = driver.find_element_by_id('id')
#for i in UserId4:
#    time.sleep( random.randrange(1, 5) / 10 )
#    id.send_keys(i)


#id.send_keys(Keys.TAB)
#time.sleep(1)


#pw = driver.find_element_by_id('pw')
#for i in UserPw4:
#     time.sleep(random.randrange(1, 5) / 10)
 #    pw.send_keys(i)


#id = driver.find_element_by_id('id')
#for i in UserId5:
#    time.sleep( random.randrange(1, 5) / 10 )
 #   id.send_keys(i)


#id.send_keys(Keys.TAB)
#time.sleep(1)

# driver.action.key_down(:shift)perform
# pw = driver.find_element_by_id('pw')
# for i in UserPw5:
#     time.sleep(random.randrange(1, 5) / 10)
 #    pw.send_keys(i)

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