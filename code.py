import pandas as pd

import requests
from bs4 import BeautifulSoup

data_excel = pd.read_excel('./image.xlsx')
lisenin = data_excel.to_dict(orient='records')
for i in lisenin:
    url = i['Url']
    name = i['Артикул']
    if url != 'nan':
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find('div', class_='product-item-detail-slider-image')
        print('---------------------------------------------------')
        string = str(quotes)
        img = 'https://vorota.moscow' + string[string.index('src="') + 5:string.index('.jpg') + 4]
        
        # image download
        print(name, url)
        p = requests.get(img)
        out = open(str(name) + '.jpg', "wb")
        out.write(p.content)
        out.close()

    