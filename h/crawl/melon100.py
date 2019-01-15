from bs4 import BeautifulSoup
import urllib.request as req




url = "https://www.melon.com/chart/index.htm"

res = req.urlretrieve(url)
#print(res)

soup = BeautifulSoup(res, "html.parser")

#print(soup)

a_list = soup.select("#lst50 > dt > div > div > div > span > a")

for a in a_list:
    title = a.string
    print(title)


b_list = soup.select("#lst50 > dt > div > div > div > a ")

for b in b_list:
    singer = b.string
    print(singer)

c_list = soup.select("#lst50 > dt > div > button > span cnt ")

for c in c_list:
    likecnt = c.string
    print(likecnt)

from selenium import webdriver
from time import sleep 


chrome_path = r"C:\chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome(C:\chromedriver_win32 (1)/chromedriver.exe)
driver.get("https://www.melon.com/chart/index.htm")
sleep(3)

driver.find_element_by_xpath("""//*[@id="tb_list"]/div/span/a""").click()

driver.quit()

a_list = soup.select("#lst50 > dt > div > div > div > span > a")

for a in a_list:
    title = a.string
    print(title)


b_list = soup.select("#lst50 > dt > div > div > div > a ")

for b in b_list:
    singer = b.string
    print(singer)

c_list = soup.select("#lst50 > dt > div > button > span cnt ")

for c in c_list:
    likecnt = c.string
    print(likecnt)
