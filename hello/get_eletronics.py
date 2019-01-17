from selenium import webdriver
from time import sleep

chrome_path = r"C:\chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?range=1&kind=3&orderClick=DAC&mallGb=KOR&linkClass=e")
sleep(0.5)

#driver.find_element_by_xpath("""//*[@id="sss0"]/li[23]/a""").click()
#posts = driver.find_elements_by_class_name("title")
#for post in posts:
#	print(post.text)

#posts = driver.find_elements_by_class_name("author")
#for post in posts:
#	print(post.text)    

posts = driver.find_elements_by_class_name("price")
for post in posts:
	print(post.text[0:10]) 

driver.find_element_by_xpath("""//*[@id="main_contents"]/div[5]/div[1]/ul/li[2]/a""").click()

sleep(0.5)

posts = driver.find_elements_by_class_name("price")
for post in posts:
	print(post.text[0:10]) 