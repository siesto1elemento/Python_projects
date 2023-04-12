import requests as r
from bs4 import BeautifulSoup as bs
import time

URL = "https://www.flipkart.com/apple-2020-macbook-air-m1-8-gb-256-gb-ssd-mac-os-big-sur-mgn63hn-a/p/itmde54f026889ce?pid=COMFXEKMGNHZYFH9&lid=LSTCOMFXEKMGNHZYFH9P56X45&marketplace=FLIPKART&q=macbook+air&store=6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&fm=organic&iid=2ad431f4-a4a1-49b6-8280-b700644d0b1d.COMFXEKMGNHZYFH9.SEARCH&ppt=hp&ppn=homepage&ssid=ayjno0oy86n6qups1681325576846&qH=b61d62051d5441f9"

while True:
    page = r.get(URL)

    soup = bs(page.content, "html.parser")

    price = soup.find("div",{"class": "_30jeq3 _16Jk6d"}).text
    print(price)
    price = price[1:]
    price_ar = price.split(",")
    price = ''.join(price_ar)
    price = int(price)
    print(price)
    if price <= 75000:
        break
    time.sleep(10)