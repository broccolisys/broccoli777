import sys
from datetime import date
# date() 함수 import 해서 뒤에서 값을 날짜로 변환하고 날짜 형식으로 포매팅 할 수 있게 함
from xlrd import open_workbook, xldate_as_tuple
# xldate_as_tuple() : 날짜, 시간, 날짜+시간 을 나타내는 엑셀의 숫자 -> 튜플 변환
# 숫자를 튜플로 변환하면 특정 날짜 요소를 추출하여 다른 날짜 형식으로 포매팅 가능
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet= output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        row_list_output = []
        for col_index in range(worksheet.ncols):
            # if-else 문을 통해 각 셀에 날짜가 들어있는지 판별 있으면 if, 없으면 else
            if worksheet.cell_type(row_index, col_index) == 3:
                # cell type 이 3번인지 판별
                # xlrd 모듈 문서(http://xlrd.readthedocs.io/en/latest/api.html?highlight=cell_type#xlrd.sheet.Cell)
                # 를 확인하면 cell type 3 은 날짜 셀임을 알수있음
                date_cell = xldate_as_tuple(worksheet.cell_value\
                    (row_index, col_index), workbook.datemode)
                # xladte_as_tuple(xldate, datemode) :
                # worksheet의 cell 값에 접근 하기 위해 cell_value 사용 뒤 row_index, col_index는
                # 위에 == 3 조건이 일치한 것과 일치
                # 이 함수의 결과는 date_cell 튜플 변수에 할당
                """dat_cell =
                (2013, 1, 1, 0, 0, 0)
                (2013, 1, 6, 0, 0, 0)
                (2013, 1, 11, 0, 0, 0)
                (2013, 1, 18, 0, 0, 0)
                (2013, 1, 24, 0, 0, 0)
                (2013, 1, 31, 0, 0, 0)
                """
                date_cell =date(*date_cell[0:3]).strftime\
                    ('%m/%d/%Y')
                """date_cell =
                01/01/2013
                01/06/2013
                01/11/2013
                01/18/2013
                01/24/2013
                01/31/2013
                """
                # tuple indexing 을  사용하여 튜플의 첫 세 요소(연도, 월, 일)에 접근하고
                # date()함수의 인수로 전달 ( 즉 값을 날짜 객체로 변환)
                # strftime() 날짜 객체를 할당된 날짜 형식의 문자열로 변환
                # ('%m/%d/%Y') 지정 날짜 형식
                row_list_output.append(date_cell)
                print(row_list_output)
                output_worksheet.write(row_index, col_index, date_cell)
            else: # 날짜가 아닌값을 차례대로 list 에 넣음
                non_date_cell = worksheet.cell_value\
                    (row_index, col_index)
                row_list_output.append(non_date_cell)
                output_worksheet.write(row_index, col_index, \
                    non_date_cell)
output_workbook.save(output_file)