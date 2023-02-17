import bs4
import urllib.request


url= 'https://www.amazon.in/Fortune-Chakki-Fresh-Atta-10kg/dp/B07DCPKZHZ/ref=sr_1_4_f3_wg?almBrandId=ctnow&fpw=alm&keywords=ata+10&qid=1659523217&s=nowstore&sprefix=ata%2Cnowstore%2C568&sr=1-4'

sauce = urllib.request.urlopen(url).read()

soup = bs4.BeautifulSoup(sauce, 'html.parser')




title = soup.find(id='productTitle').get_text().strip()
prices = soup.find(id='priceblock_ourprice').get_text().strip()

print(prices)

# print(f'Price of {title} is {prices}.')
