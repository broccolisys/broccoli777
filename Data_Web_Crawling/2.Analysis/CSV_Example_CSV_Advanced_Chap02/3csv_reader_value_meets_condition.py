"""특정 조건을 충족하는 행의 필터링-기본"""
# 두가지 조건에 부합하는 행의 값을 판별하고, 그 조건을 충족하는 행으로 구성된 하위 데이터셋을
# 출력파일로 작성하는 방법

import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        # next fuction 이용 input_file의 first line을 header라는 list variable로 할당
        filewriter.writerow(header)
        for row_list in filereader:
            # column value 를 가지고 옴
            supplier = str(row_list[0]).strip()
            # list indexing해서 각 row의 first column(Supplier Name)의 value를 가져와서 string으로 변환
            # 다음 strip function 을 이용해서 양끝 공백, 탭, 개행문자 제거 후 supplier variable에 저장
            cost = str(row_list[3]).strip('$').replace(',','')
            # 각 row 의 fourth column의 value 를 가져온 다음 string 으로 변환
            # strip을 통해 문자열에서 $ 제거 후, replace function 이용 쉼표(,) 제거 후 cost variable 저장
            if supplier == 'Supplier Z' or float(cost) > 600.0:
            # supplier name이 'Supplier Z' 이거나 또는 cost 가 $600.00 이상인 행만 필터링
                filewriter.writerow(row_list)