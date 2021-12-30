import pandas as pd

data_excel = pd.read_excel('./image.xlsx')
lisenin = data_excel.to_dict(orient='record')
for i in lisenin:
    print(i['Артикул'], i['Наименование'])