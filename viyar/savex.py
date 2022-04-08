import pandas as pd
from sqlalchemy import false

def save_excel(table, table_f, file_name):
    """    
    table.to_excel('C:\\Users\\Matushev_work\\Desktop\\СОХРАН\\bazis\\output.xlsx', index=False)         #WORK rewrites existing file
    table_f.to_excel('C:\\Users\\Matushev_work\\Desktop\\СОХРАН\\bazis\\output_f.xlsx', index=False)         #WORK rewrites existing file
    #table.to_excel('C:\\Users\\Admin\\Desktop\\СОХРАНЕНИЕ\\bazis\\output.xlsx', index=False)         #HOME rewrites existing file
    """
    """
    writer_initial = pd.ExcelWriter('C:\\Users\\Matushev_work\\Desktop\\СОХРАН\\bazis\\output.xlsx', engine='xlsxwriter')
    writer_initial_f = pd.ExcelWriter('C:\\Users\\Matushev_work\\Desktop\\СОХРАН\\bazis\\output_f.xlsx', engine='xlsxwriter')
    table.to_excel(writer_initial, index=False, sheet_name='Result')
    table_f.to_excel(writer_initial_f, index=False, sheet_name='Result')
    writer_initial.save()
    writer_initial_f.save()    
    """
    #writer = pd.ExcelWriter(f'C:\\Users\\Matushev_work\\Desktop\\СОХРАН\\bazis\\out{file_name}.xlsx', engine='xlsxwriter')
    writer_f = pd.ExcelWriter(f'C:\\Users\\Matushev_work\\Desktop\\СОХРАН\\bazis\\out {file_name}.xlsx', engine='xlsxwriter')
    #table.to_excel(writer, index=False, sheet_name='Result')
    table_f.to_excel(writer_f, index=False, sheet_name='Result')

    #workbook = writer.book
    workbook_f = writer_f.book
    #worksheet = writer.sheets['Result']
    worksheet_f = writer_f.sheets['Result']

    for column in table:
        col_width = max(table[column].astype(str).map(len).max(), len(column))*1.1
        col_idx = table.columns.get_loc(column)
        #worksheet.set_column(col_idx, col_idx, col_width)
        worksheet_f.set_column(col_idx, col_idx, col_width)
     
    #fig_fmt = workbook.add_format({'num_format':'0,0', 'align':'center', 'bold':False})
    fig_fmt_f = workbook_f.add_format({'num_format':'0.00', 'align':'center', 'bold':False})    
    
    #worksheet.set_column('C:E', 15, fig_fmt)
    worksheet_f.set_column('C:E', 15, fig_fmt_f)
    
        
    #writer.save()
    writer_f.save()    

    print("Files succesfully saved!")