from bs4 import BeautifulSoup
import requests

# url = "https://blog.naver.com/korea_diary/221433346994"
url = "https://blog.naver.com/PostView.nhn?blogId=korea_diary&logNo=221433346994&redirect=Dlog&widgetTypeCall=true&topReferer=https%3A%2F%2Fwww.naver.com%2F&directAccess=false"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# sel = "img"
sel = "#SE-e3efce8c-f39b-4c97-9291-a933aa1763bd > div > div > a > img"

imgs = soup.select(sel)
print(imgs, len(imgs))

if len(imgs) < 1:
    exit()

img = imgs[0]
src = img.get('src')
print("img>>", src)


# for link in links:
#     if "http" in link.get('src'):
#         lnk = link.get('src')
#         with open(basename(lnk), "wb") as f:
#             f.write(requests.get(lnk).content)