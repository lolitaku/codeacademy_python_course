import csv

from bs4 import BeautifulSoup
import requests

source = requests.get('https://shop.telia.lt/telefonai/?filter=brand:samsung').text
soup = BeautifulSoup(source, 'html.parser')

blokai = soup.find_all('div', class_ = 'mobiles-product-card card card__product card--anim js-product-compare-product')

for blokas in blokai:
    print(blokas.text.strip().replace("\n", ""))
    # grazina stringa o replace panaikina n naujas eilutes

    # name = blokas.find("a", class_ = "mobiles-product-card__title js-open-product").text.strip()
    # print(name)

    # monthly_price = blokas.find("div", class_ = "mobiles-product-card__price-marker").text.strip()
    # print(monthly_price)

    # price = blokas.find("div", class_ = "mobiles-product-card__full-price price")\
    # .find("div", class_ = "mobiles-product-card__price-marker").text.strip()

    # print(price)
    # print("--------")

    

with open("Telia Samsung telefonai.csv", "w", encoding="UTF-8", newline='') as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(['Modelis', 'Mėnesio kaina', 'Kaina'])

    for blokas in blokai:
        try:
            name = blokas.find("a", class_ = "mobiles-product-card__title js-open-product").text.strip()
            print(name)
            monthly_price = blokas.find("div", class_ = "mobiles-product-card__price-marker").text.strip()
            print(monthly_price)
            price = blokas.find("div", class_ = "mobiles-product-card__full-price price")\
             .find("div", class_ = "mobiles-product-card__price-marker").text.strip()
            csv_writer.writerow([name, monthly_price, price])
        except:
            pass

        