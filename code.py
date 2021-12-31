import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image

data_excel = pd.read_excel(input("Укажите путь к excel файлу: "))
url_save = input('Укажите места для сохранения изображений: ')
lisenin = data_excel.to_dict(orient='records')
for i in lisenin:
    try:
        url = i['Url']
        name = i['Артикул']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find('div', class_='product-item-detail-slider-image')
        print('---------------------------------------------------')
        string = str(quotes)
        file = 'https://vorota.moscow' + string[string.index('src="') + 5:string.index('.jpg') + 4]
        
        # image download
        print(name, url)
        p = requests.get(file)
        out = open(url_save + str(name) + '.jpg', "wb")
        out.write(p.content)
        out.close()
    except:
        print('nan')
    