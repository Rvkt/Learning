import urllib
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Crucial-BX500-240GB-2-5-inch-CT240BX500SSD1/dp/B07G3YNLJB/ref=pd_bxgy_sccl_1/258-7081387-2843855?pd_rd_w=wfMTT&content-id=amzn1.sym.d68c4347-8b80-4998-9474-4671a1e32e96&pf_rd_p=d68c4347-8b80-4998-9474-4671a1e32e96&pf_rd_r=9XA47A6FWBTW45NHRFX8&pd_rd_wg=7Lwnq&pd_rd_r=2c736e23-9ddc-448b-8d53-679661d755d9&pd_rd_i=B07G3YNLJB&th=1'

headers = dict({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",})


# def sum_dict(var: dict):
#     return sum(var[key] for key in var.keys())


page = urllib.request.urlopen(URL).read()

soup = BeautifulSoup(page.content, 'html.parser')

print(soup)

# title = soup.find(id="productTitle").getText().strip()


# # price = soup.find("class='a-offscreen'")
# price = soup.find_all(id="class(.a-price-whole)")

# print(title)
# print(price)


# print(soup.prettify())