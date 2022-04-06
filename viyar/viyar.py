from email import header
import pandas as pd

table = pd.read_html("C:\\Users\\Admin\\Desktop\\СОХРАНЕНИЕ\\bazis\\1.html", header=0)[0].iloc[:,1:4:].drop(labels=13, axis=0)

# print(table)

for i in range(table.shape[0]):
    val = table.at[i,'Количество']
    table.at[i,'Количество'] = float(val[:-3] + '.' + val[-3:])

#print(table)

to_str = lambda x: (str(x)) #функция для обработки данных столбца

prices = pd.read_csv("price.csv", sep=";", converters={'Код':to_str})

#print(prices)

#Добавление столбца с ценой по кодам товаров из прайса
for i in range(table.shape[0]):

    #print('Code in table ' + table.at[i, 'Код'])

    filter = prices['Код'] == table.at[i, 'Код']

    #print(prices.loc[filter]['Цена'])
    
    table.at[i,'Цена'] = float(prices.loc[filter]['Цена'])      # Добавление столбца с ценой из прайса по коду товара
    
    table.at[i,'Товар'] = prices.loc[filter]['Товар'].to_string().split('    ')[1]          # Замена украинских наименований товаров на русские
    #print(prices.loc[filter]['Товар'].to_string().split('    ')[1])
    table.at[i, 'Стоимость'] = table.at[i,'Количество'] * table.at[i,'Цена']            # Добавление столбца со стоимость позиции (количество х цена)

finish_row = {'Код':'','Товар':'','Количество':'','Цена':'Итого','Стоимость':table['Стоимость'].sum()}          # Добавление строки с итоговой стоимостью
table = table.append(finish_row, ignore_index=True)

print(table)

ex_writer = pd.ExcelWriter("C:\\Users\\Admin\\Desktop\\СОХРАНЕНИЕ\\bazis\\1.xlsx")       # Создание моодуля записи в Excel
table.to_excel(ex_writer)                                                                   # Запись в Excel
ex_writer.save()                                                                            # Сохраниение файла Excel