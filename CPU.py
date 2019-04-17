from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books"

# opeining up connection, grabbing the page

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing

page_soup = soup(page_html, "html.parser")

# grabs each product

containers = page_soup.findAll("div", {"class":"a-section a-spacing-none aok-relative"})

filename = "products.csv"
f = open(filename, "w")


headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
    #try:

    containers = container.div.div.a.img["alt"]
        
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