from bs4 import BeautifulSoup
from notifier import Notifier
import os
import requests

ACCEPT_LANGUAGE = os.environ['ACCEPT_LANGUAGE']
USER_AGENT = os.environ['USER_AGENT']

webpage = "https://www.amazon.com/Yves-Saint-Laurent-Collections-1962-2002/dp/0300243650/ref=zg_bs_1862_sccl_38/143-9746091-4817013?psc=1"
headers = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT
}
response = requests.get(url=webpage,
                        headers=headers)
amazon_webpage = response.text
soup = BeautifulSoup(amazon_webpage, "html.parser")

price = float(soup.find(class_="a-size-base a-color-price a-color-price").getText().split()[0].replace("$",""))
product_name = soup.find(id="productTitle").getText()

notification = Notifier()

if price < 45:
    notification.send_email(product_name, price, webpage, "tripon.maria06@gmail.com")


