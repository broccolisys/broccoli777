"""2.11 파일에서 데이터 값의 합계 및 평균 계산하기-기본"""

import csv
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

output_header_list = ['file_name', 'total_sales', 'average_sales']
# 출력 파일의 열 헤더가 포함된 리스트 생성
csv_out_file = open(output_file, 'a', newline='')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header_list) # header_list 저장

for input_file in glob.glob(os.path.join(input_path,'sales_*')):
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        output_list = [] # 결과 값을 저장할 리스트 생성 , 입력 파일의 이름이 저장될 리스트
        output_list.append(os.path.basename(input_file))
        header = next(filereader)
        total_sales = 0.0
        number_of_sales = 0.0
        for row in filereader: # 입력 파일의 데이터 행을 반복하는 for 문
            sales_amount = row[3]
            total_sales += float(str(sales_amount).strip('$').replace(',',''))
            # str() 를 이용해서 sales_amount 값이 문자열인지 확인한 후,
            # strip() , replace() 사용하여 데이터 값에서 달러기호와 쉼표 제거
            # 그다음 float() 이용 값을 부동 소수점 숫자로 변환한 뒤,
            # 이 값을 total_sales 값에 더한다
            number_of_sales += 1.0
        average_sales = '{0:.2f}'.format(total_sales / number_of_sales)
        # 평균 매출을 구해서 소수점 이하 두자리로 형식화
        output_list.append(total_sales)
        output_list.append(average_sales)
        filewriter.writerow(output_list)
csv_out_file.close()