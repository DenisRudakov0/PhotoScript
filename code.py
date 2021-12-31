import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image
import os
from PIL import Image, ImageChops

def download_image(data_excel, url_save):
    lisenin = data_excel.to_dict(orient='records')
    counter = 0
    for i in lisenin:
        try:
            url, name = i['Url'], i['Артикул']
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find('div', class_='product-item-detail-slider-image')
            string = str(quotes)
            file = 'https://vorota.moscow' + string[string.index('src="') + 5:string.index('.jpg') + 4]
            
            # image download
            p = requests.get(file)
            out = open(url_save + str(name) + '.jpg', "wb")
            out.write(p.content)
            out.close()
            counter += 1
            print(name, url)
        except:
            print(name, 'Не имеет ссылки на изображение')
        print('---------------------------------------------------')
    return counter

def difference_img(path):
    imgs=tuple(os.listdir(path))
    NoImage = './NoImage.jpg'
    image_none = Image.open(NoImage)
    counter = 0
    for i in imgs:
        image = Image.open(path + i)
        result=ImageChops.difference(image_none, image).getbbox()
        if result==None:
            os.remove(path + i)
            print(image_none, path + i,'Не имеет изображение')
            counter += 1
    return counter

data_excel = pd.read_excel(input("Укажите путь к excel файлу: "))
url_save = input('Укажите места для сохранения изображений: ')

parse_img = download_image(data_excel, url_save)
del_img = difference_img(url_save)
print('Было спарсено ' + str(parse_img) + ' изображений. Из них ' + str(del_img) + ' не имели изображений и были удалены.')


