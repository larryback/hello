from bs4 import BeautifulSoup
import requests

url = "https://www.skyscanner.net/transport/flights/sela/syda?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1902&selectedoday=01"

selector = "table.bpk-calendar-grid-2GXun tbody tr"

html = requests.get(url).text

with open("./data/just_test.html", mode="w") as file:
    file.write(html)

soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

print(soup.select(selector))
