from selenium import webdriver
from time import sleep

chrome_path = r"C:\chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?range=1&kind=3&orderClick=DAC&mallGb=KOR&linkClass=e")
sleep(3)

#driver.find_element_by_xpath("""//*[@id="sss0"]/li[23]/a""").click()
posts = driver.find_elements_by_class_name("title")
for post in posts:
	print(post.text)


exit()
posts = driver.find_elements_by_class_name("author")
for post in posts:
	print(post.text[0:4])    
# 출판사  걸러 내는법 |  |  |  나뉘어 있을때


posts = driver.find_elements_by_class_name("price")
for post in posts:
	print(post.text[0:10]) 



driver.find_element_by_xpath("""//*[@id="main_contents"]/div[5]/div[1]/ul/li[2]/a""").click()

sleep(5)

#  다음 페이지에서  웹드라이버  작동 시키기. +  읽은 내용 저장하기
posts = driver.find_elements_by_class_name("title")
print(">>>", posts)
for post in posts:
	print(post.text)


posts = driver.find_elements_by_class_name("author")
print(">>>", posts)
for post in posts:
	print(post.text[0:4])  


posts = driver.find_elements_by_class_name("price")
print(">>>", posts)
for post in posts:
	print(post.text[0:10]) 

driver.quit()


with open ("filename", "w", encoding = "euc-kr" ) as file:
    file.write(price)  


a=[]
for post in posts:    
    a.append(i)

driver.quit()
