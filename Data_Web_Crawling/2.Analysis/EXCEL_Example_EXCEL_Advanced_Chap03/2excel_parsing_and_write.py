import sys
from xlrd import open_workbook
# xlrd : excel 파일을 읽는 library
from xlwt import Workbook
# xlwt : excel 파일을 쓰는 library

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook() # 객체를 인스턴스화하여 결과를 출력하여 excel 를 쓸수있음
output_worksheet = output_workbook.add_sheet('jan_2013_output')
# xlwt의 add_sheet() 함수를 사용하여 excel 안에 worksheet 추가

with open_workbook(input_file) as workbook: # input_file 을 염
    worksheet = workbook.sheet_by_name('january_2013') # input_file 안 january_2013 sheet 로 감
    for row_index in range(worksheet.nrows): # january_2013 worksheet 의 row 갯수 를 range 돌림
        for column_index in range(worksheet.ncols): # january_2013 worksheet 의 column 갯수 를 range 돌림
            output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))

output_workbook.save(output_file)
