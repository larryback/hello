import os
import csv
import sys

from openpyxl import Workbook
import imp



imp.reload(sys)
#sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    workbook = Workbook()
    worksheet = workbook.active
    with open("melon_top_100.csv", 'r', "CP949") as f:
        reader = csv.reader("./melon_top_100.csv")
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                for idx, val in enumerate(col.split(',')):
                    cell = worksheet.cell(row=r+1, column=c+1)
                    cell.value = val
    workbook.save("melontop100.xlsx")