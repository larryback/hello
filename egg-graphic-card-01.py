import urllib.request
import bs4

url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")

print(html.read())
#print("----------------------------------------------------------------------------------")
#print(bsObj)

brand = bsObj.find("div", {"class":"item-branding"})
#print("----------------------------------------------------------------------------------")
#print(brand)
#print("----------------------------------------------------------------------------------")
#brand_a = brand.find("a")
#print(brand_a.title)



print("----------------------------------------------------------------------------------")
#brand_A = bsObj.find("a", {"class":"item-brand"}, "img" > "attr", "alt"  )
brand_A = bsObj.find("a", {"class":"item-brand"}, "img"> "attr" "alt= * ")
#$(‘img’).attr(‘alt’) 
print(brand_A)

