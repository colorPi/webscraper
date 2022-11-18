import requests
import lxml
from bs4 import BeautifulSoup

#URL = "https://www.amway.com.vn/vn/c/dinh-duong-va-suc-khoe"
#page = requests.get(URL)

htmlFile = open('dingduongvasuckhoe.html', encoding="utf8")
soup = BeautifulSoup(htmlFile, "lxml")

results = soup.find('div', class_='productsContainer')
products = results.find_all('div', class_='productListDetailsWrapper')

for product in products:
    productName = product.find('p', class_='productName')
    productDescription = product.find('p', class_='productDescription')
    productPrice = product.find('span', class_='productPrice')
        
    print(productName.text.strip())
    try:
        print(productDescription.text.strip()[-6:])
    except:
        productDescription = 'NA'
        print(productDescription)
    try:
        print(productPrice.text.strip()[:-1].replace('&nbsp;', ''))
    except:
        productPrice = 'NA'
        print(productPrice)
    print()