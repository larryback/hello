from selenium import webdriver
import time 



chrome_path = r"C:\chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("http://mobile.kyobobook.co.kr/")


driver.find_element_by_xpath("""//*[@id="BannerappDown"]/span[1]/img""").click()

# 베스트 
driver.find_element_by_xpath("""//*[@id="content"]/div[1]/ul/li[3]/button/span""").click()

time.sleep(6)
#driver.find_element_by_xpath("""//*[@id="sss0"]/li[23]/a""").click()
posts = driver.find_elements_by_class_name("tit")
for post in posts:
	print(post.text)
#종합주간
driver.find_element_by_xpath("""//*[@id="mainTab_3"]/div[1]/ul/li[2]/a/strong""").click()
time.sleep(6)






driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")





driver.find_element_by_xpath("""//*[@id="bestDaily"]/div[2]/div[2]/button/span""").click()


driver.find_element_by_xpath("""//*[@id="bestDaily"]/div[3]/div[3]/button/span""").click()









time.sleep(10)
posts = driver.find_elements_by_class_name("tit")
for post in posts:
	print(post.text)






#exit()
#posts = driver.find_elements_by_class_name("price")
#for post in posts:
	#print(post.text[0:4])    
# 출판사  걸러 내는법 |  |  |  나뉘어 있을때


#posts = driver.find_elements_by_class_name("average")
#for post in posts:
#	print(post.text[0:10]) 



#driver.find_element_by_xpath("""//*[@id="main_contents"]/div[5]/div[1]/ul/li[2]/a""").click()

sleep(5)

#  다음 페이지에서  웹드라이버  작동 시키기. +  읽은 내용 저장하기
#posts = driver.find_elements_by_class_name("title")
#print(">>>", posts)
#for post in posts:
	#print(post.text)


#posts = driver.find_elements_by_class_name("author")
#print(">>>", posts)
#for post in posts:
	#print(post.text[0:4])  


#posts = driver.find_elements_by_class_name("price")
#print(">>>", posts)
#for post in posts:
	#print(post.text[0:10]) 

#driver.quit()


#with open ("filename", "w", encoding = "euc-kr" ) as file:
    #file.write(price)  


a=[]
for post in posts:    
    a.append(i)

driver.quit()