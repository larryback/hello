import urllib.request 
import bs4

url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")

print(html.read())
print(bsObj)

branding = bsObj.find("div", {"class":"item-branding"})
#print("------------------------------------------------")
#print(branding)
print("------------------------------------------------")
branding_a = bsObj.find("div", {"class":"item-branding"}, "a")