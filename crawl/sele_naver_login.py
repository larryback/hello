import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drvPath = '/Users/jade/workspace/python/chromedriver'
driver = webdriver.Chrome(drvPath)
UserId = "jeonseon"
# UserPw = "!mD:L76YQn.Bfa7"

driver.get("https://www.naver.com")
time.sleep(1)

driver.find_element_by_class_name('lg_local_btn').click()
print("click big button!!")
time.sleep(1)

id = driver.find_element_by_id('id')
for i in UserId:
    time.sleep( random.randrange(1, 5) / 10 )
    id.send_keys(i)

# id.send_keys(Keys.TAB)
# time.sleep(1)

# pw = driver.find_element_by_id('pw')
# for i in UserPw:
#     time.sleep(random.randrange(1, 5) / 10)
#     pw.send_keys(i)

# time.sleep(0.5)
# pw.send_keys(Keys.RETURN)

# time.sleep(1)


time.sleep(5)                # cf.  driver.implicitly_wait(5)
# driver.quit() # driver.close()
