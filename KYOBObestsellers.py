from bs4 import BeautifulSoup
import urllib.request as req
import time
url = "http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?range=1&kind=0&orderClick=DAA&mallGb=KOR&linkClass=A"

res = req.urlopen(url)
#print(res)



soup = BeautifulSoup(res, "html.parser")



#print(soup)

a_list = soup.select("#maincontents > ul > li > div > div > a > strong")

for a in a_list:
    title = a.string
    print(title)


b_list = soup.select("#maincontents > ul > li > div > div.author ")

for b in b_list:
    author = b.string
    print(author) 


c_list = soup.select("#maincontents > ul > li > div > div.line ")

for c in c_list:
    publisher = c.string
    print(publisher) 

chrome_path = r"C:\chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome("C:\chromedriver_win32 (1)/chromedriver.exe")
driver.get("https://www.melon.com/chart/index.htm")
time.sleep(3)

driver.find_element_by_xpath("""//*[@id="main_contents"]/div[5]/div[1]/ul/li[2]/a""").click()

a_list = soup.select("#maincontents > ul > li > div > div > a > strong")

for a in a_list:
    title = a.string
    print(title)


b_list = soup.select("#maincontents > ul > li > div > div.author ")

for b in b_list:
    author = b.string
    print(author) 


c_list = soup.select("#maincontents > ul > li > div > div.line ")

for c in c_list:
    publisher = c.string
    print(publisher) 

chrome_path = r"C:\chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome("C:\chromedriver_win32 (1)/chromedriver.exe")
driver.get("https://www.melon.com/chart/index.htm")
time.sleep(3)

driver.find_element_by_xpath("""//*[@id="main_contents"]/div[5]/div[1]/ul/li[2]/a""").click()



a_list = soup.select("#maincontents > ul > li > div > div > a > strong")

for a in a_list:
    title = a.string
    print(title)


b_list = soup.select("#maincontents > ul > li > div > div.author ")

for b in b_list:
    author = b.string
    print(author) 


c_list = soup.select("#maincontents > ul > li > div > div.line ")

for c in c_list:
    publisher = c.string
    print(publisher) 


chrome_path = r"C:\chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome("C:\chromedriver_win32 (1)/chromedriver.exe")
driver.get("https://www.melon.com/chart/index.htm")
time.sleep(3)

driver.find_element_by_xpath("""//*[@id="main_contents"]/div[5]/div[1]/ul/li[4]/a""").click()

a_list = soup.select("#maincontents > ul > li > div > div > a > strong")

for a in a_list:
    title = a.string
    print(title)


b_list = soup.select("#maincontents > ul > li > div > div.author ")

for b in b_list:
    author = b.string
    print(author) 


c_list = soup.select("#maincontents > ul > li > div > div.line ")

for c in c_list:
    publisher = c.string
    print(publisher) 

chrome_path = r"C:\chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome("C:\chromedriver_win32 (1)/chromedriver.exe")
driver.get("https://www.melon.com/chart/index.htm")
time.sleep(3)

driver.find_element_by_xpath("""//*[@id="main_contents"]/div[5]/div[1]/ul/li[5]/a""").click()

a_list = soup.select("#maincontents > ul > li > div > div > a > strong")

for a in a_list:
    title = a.string
    print(title)


b_list = soup.select("#maincontents > ul > li > div > div.author ")

for b in b_list:
    author = b.string
    print(author) 


c_list = soup.select("#maincontents > ul > li > div > div.line ")

for c in c_list:
    publisher = c.string
    print(publisher) 
