import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image
import os
from PIL import Image, ImageChops

def download_image(data_excel, url_save):
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

def difference_img(path):
    imgs=tuple(os.listdir(path))
    print(imgs)
    NoImage = './NoImage.jpg'
    image_none = Image.open(NoImage)
    for i in imgs:
        image = Image.open(path + i)
        result=ImageChops.difference(image_none, image).getbbox()
        if result==None:
            os.remove(path + i)
            print(image_none, path + i,'matches')

# data_excel = pd.read_excel(input("Укажите путь к excel файлу: "))
url_save = input('Укажите места для сохранения изображений: ')
# C:\Users\Denis\Desktop\image_download\code\image.xlsx
# C:\Users\Denis\Desktop\test_image\
# download_image(data_excel, url_save)
difference_img(url_save)


