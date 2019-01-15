from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?range=1&kind=2&orderClick=DAB&mallGb=KOR&linkClass=A"

# opeining up connection, grabbing the page

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing

page_soup = soup(page_html, "html.parser")

# grabs each product

containers = page_soup.findAll("div", {"class":"title"})

filename = "products.csv"
f = open(filename, "w")


headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
    #try:

    brand = container.div.div.img["alt"]
        
    #except AttributeError:
        #pass    
    
    title_container = container.findAll("a", {"class":"item-title"}) 
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()  
    
    try:

        print("brand: " + brand)

    except NameError:
        pass    
    print("product_name " + product_name)
    print("shipping " + shipping)

    try:

        f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")
    except NameError:
        pass    

f.close()    