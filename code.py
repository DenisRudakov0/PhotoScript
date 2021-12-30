import pandas as pd

data_excel = pd.read_excel('./image.xlsx')
data_excel.head()
print(data_excel)
for i in data_excel:
    print(i)

print('ok')