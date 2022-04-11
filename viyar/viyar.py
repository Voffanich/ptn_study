import pandas as pd
from savex import save_excel
import os

# Определяем файлы *.html в папке
dirname = 'C:\\Users\\Matushev_work\\Desktop\\СОХРАН\\bazis'
dirfiles = os.listdir(dirname)

files = []
paths = []
count = 1

for fil in dirfiles:
    if str(fil).endswith('html'): 
        files.append(fil)       
        paths.append(os.path.join(dirname, fil)) 
        print(str(count)+'. '+str(fil))
        count += 1
        
file_to_process = int(input('Введите номер файла для обработки: '))-1


#table = pd.read_html("C:\\Users\\Admin\\Desktop\\СОХРАНЕНИЕ\\bazis\\1.html", header=0)[0].iloc[:,1:4:]         #home
table = pd.read_html(paths[file_to_process], header=0)[0].iloc[:,1:4:]      #work
table.drop(labels=table.shape[0]-1, axis=0, inplace=True)       # удаление последней строки с Итого
table_e = table.copy(deep=True)

for i in range(table.shape[0]):
    val = table.at[i,'Количество']
    table.at[i,'Количество'] = float(val[:-3] + '.' + val[-3:])

# print(table)

to_str = lambda x: (str(x)) #функция для обработки данных столбца

# prices = pd.read_csv("price.csv", sep=";", converters={'Код':to_str})
prices = pd.read_csv("price.csv", sep=";", dtype={'Код':str})

#print(prices)

#Добавление столбца с ценой по кодам товаров из прайса
for i in range(table.shape[0]):
    if i == 0:                                                                                  # Обработка кода ДСП
        table.at[i,'Цена'] = int(input('Введите стоимость листа ДСП:'))                                                              # Добавление столбца с ценой ДСП
        table.at[i,'Товар'] = 'ДСП'                                                             # Замена украинского название на русское
        table.at[i, 'Стоимость'] = table.at[i,'Количество'] * table.at[i,'Цена']                # Добавление столбца со стоимость позиции (количество х цена)
    else:
        filter = prices['Код'] == table.at[i, 'Код']
        table.at[i,'Цена'] = float(prices.loc[filter]['Цена'])                                  # Добавление столбца с ценой из прайса по коду товара
        table.at[i,'Товар'] = prices.loc[filter]['Товар'].to_string().split('    ')[1]          # Замена украинских наименований товаров на русские
        table.at[i, 'Стоимость'] = table.at[i,'Количество'] * table.at[i,'Цена']                # Добавление столбца со стоимость позиции (количество х цена)

table_f = table.copy(deep=True)                                                                 # Копирование таблицы
for i in range(table.shape[0]):                                                                 # Замена столбца со значениями на формулы
     table_f.at[i, 'Стоимость'] = '=C' + str(i+2) + '*D' + str(i+2)
     
finish_row = {'Код':'','Товар':'','Количество':'','Цена':'Итого','Стоимость':table['Стоимость'].sum()}          # Добавление строки с итоговой стоимостью в таблицу со значениями
finish_row_f = {'Код':'','Товар':'','Количество':'','Цена':'Итого','Стоимость':f'=СУММ(E2:E{table_f.shape[0]+1})'}          # Добавление строки с итоговой стоимостью в таблицу со значениями
fr = pd.DataFrame(finish_row, index=[table.shape[0]])
fr_f = pd.DataFrame(finish_row_f, index=[table_f.shape[0]])
table = pd.concat([table,fr],axis=0)
table_f = pd.concat([table_f,fr_f],axis=0)

print(table)

save_excel(table, table_f, str(files[file_to_process]).replace('.html',''))
