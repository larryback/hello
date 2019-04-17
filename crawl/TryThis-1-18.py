import openpyxl
from pprint import pprint

book = openpyxl.load_workbook("./melon_top_100.csv")
sheet = book.worksheets[0]

data = []
for r in sheet.rows:
    data.append([ r[0].value, r[1].value, r[3].value ])

#del data[0]    # header 제거

data = sorted(data, key=lambda x: x[2], reverse=True)
pprint(data)
book.save("./Melon_top_100.xlsx")

from pyexcel.cookbook import merge_all_to_a_book
# import pyexcel.ext.xlsx # no longer required if you use pyexcel >= 0.2.2 
import glob


merge_all_to_a_book(glob.glob("your_csv_directory/*.csv"), "output.xlsx")