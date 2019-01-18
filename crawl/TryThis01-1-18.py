#    from pyexcel.cookbook import merge_all_to_a_book
    # import pyexcel.ext.xlsx # no longer required if you use pyexcel >= 0.2.2 
#    import glob


#    merge_all_to_a_book(glob.glob("your_csv_directory/*.csv"), "output.xlsx")

#import pandas as pd

#filepath_in = "./melon_top_100.csv"
#filepath_out = "./Melon_top_100.xlsx"
#pd.read_csv(filepath_in, delimiter=";", encoding = euc-kr).to_excel(filepath_out)

#pd.read_csv('./melon_top_100.csv')
#.to_excel('Melon_top_100.xlsx')

import openpyxl 
import csv 

examplefile = open('./melon_top_100.csv') 
exampleReader = csv.reader(examplefile) 
exampleData = list(exampleReader) 


wb = openpyxl.load_workbook('open.xlsx') 
ws = wb.get_sheet_by_name('Sheet1') 

for i in range (1,9): 
    for h in range(1, 5): 
     a = i-1 
     b = h-1 
     ws.cell(row=i, column=h).value = exampleData[a][b] 


wb.save('./Melon_top_100.xlsx') 