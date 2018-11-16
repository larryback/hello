from bs4 import BeautifulSoup
import requests

url = "https://play.google.com/store/apps/category/GAME/collection/topselling_paid?hl=koTL%3BDR"
res = requests.get(url)

soup = BeautifulSoup(res. text, 'html.parser')
card_list = soup.select('div.card-list')

print(">>>>>>>>", len(card_list), card_list[0].get('class'))

for i in card_list:

    cards = i.select('.card')
    print("LLL>>", len(cards))

    for c in cards:
        title = c.select('a.title')[0].text.strip()
        subtitle = c.select('a.subtitle')[0].get('title')
        print(">>", c.get('class'), [title, subtitle])