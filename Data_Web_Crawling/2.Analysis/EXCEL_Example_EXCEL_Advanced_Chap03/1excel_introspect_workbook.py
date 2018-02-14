"""3.1 엑셀 통합 문서 내부 살펴보기"""

import sys
from xlrd import open_workbook

input_file = sys.argv[1]

workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
# .nsheets : sheet 갯수

for worksheet in workbook.sheets():
    # .sheets 를 해서 sheet 내용을 가지고 와서 worksheet 할당
    print("Worksheet name:", worksheet.name, "\tRows:",\
          worksheet.nrows, "\tColumns:", worksheet.ncols)
    #worksheet의 이름, 행, 열 갯수를 가지고 옴
