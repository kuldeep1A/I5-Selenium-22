import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

URL = "https://www.amazon.in/s?k=bags&page="
PRODUCT_URL = "https://www.amazon.in/"
Headers = {
    'Accept-Language':"en-US,en;q=0.9",
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
}

PRODUCTS = []
page = 0
while page < 20:
    print(f"Page No {page}")
    response = requests.get(url=f"{URL}{page}", headers=Headers)
    amazon_web_page = response.text

    # Create a Soup to access html parser
    soup = BeautifulSoup(amazon_web_page, "html.parser")

    links = soup.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})

    print(len(links))
    for link in links:
        try:
            product_asin = link.get('data-asin')
            product_url = f"{PRODUCT_URL}{link.a.get('href')}"
            product_name = link.h2.text
            product_price = link.find('span', {'class': 'a-offscreen'}).get_text().replace(',', '').strip('₹')
            product_rating = link.find('span', {'class': 'a-icon-alt'}).get_text().split(' ')[0]
            product_review = link.find('span', {'class': 'a-size-base'}).get_text().replace(',', '')
            PRODUCTS.append([product_url, product_name, product_rating, product_review, product_asin])
        except AttributeError:
            continue
    page += 1
    sleep(1.5)
    print(PRODUCTS)
for index, link in enumerate(PRODUCTS):
    response_page = requests.get(url=link[0], headers=Headers)
    product_page = response_page.text
    # Again create second soup for access own-s products
    soup2 = BeautifulSoup(product_page, "html.parser")
    try:
        dec_list = soup2.find('div', {'id': 'featurebullets_feature_div'})
        pro_description = soup2.find('div', {'id': 'productDescription'}).get_text().strip()
        description = [desc.get_text().strip() for desc in dec_list.find_all('li')]
        description = ''.join(description)

        pro_list = soup2.find('div', {'id': 'detailBulletsWrapper_feature_div'})
        details = pro_list.find_all('li')
        manufacturer = ''
        for detail in details:
            if 'Manufacturer' in detail.text and 'Discontinued' not in detail.text:
                manufacturer = detail.text.split(':')[-1].split()[1:]
                manufacturer = ' '.join(manufacturer)
                break

        PRODUCTS[index].append(link.extend([description, manufacturer, pro_description]))
    except AttributeError:
        continue
    sleep(1.5)
    PRODUCTS[index]= PRODUCTS[index][:-1]
    print(PRODUCTS[index])


df = pd.DataFrame(PRODUCTS, columns=["product url", "product name", "product price", "rating", "number of reviews", "asin", "description", "manufacturer", "product description"])
df.to_csv('amazon.csv', index=False)
