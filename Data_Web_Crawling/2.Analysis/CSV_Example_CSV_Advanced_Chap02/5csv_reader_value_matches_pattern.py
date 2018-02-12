"""패턴/정규 표현식을 활용한 필터링-기본
특정한 패턴과 일치하거나 패턴이 포함되어 있는 행을 선택하여 하위 데이터셋으로 만들어야 하는경우
정규표현식을 사용한다.
"""

import csv
import re
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)
# r은 작은따옴표 사이의 pattern이 원시 문자열임을 나타냄
# ?P<>을 통해서 이름을 지어주거나 화면에 출력하게 해줌
# ^로 인해 찾을려고 하는 pattern 은 무조건 001-가 오며,
# .*로 인해 뒤에 오는거는 아무거나 0회이상 다 온다는걸 포함
# re.I 는 대소문자 구분 없다는것을 의미

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            invoice_number = row_list[1]
            # row_list의 행 data 중 [1] 의 indexing에 해당하는 열 값을 가지고 와서
            # invoice_number varibable 로 할당
            if pattern.search(invoice_number): # 저장된 값의 pattern 을 찾음
                filewriter.writerow(row_list) # 일치하는 경우 저장

"""
row_list = 
['Supplier X', '001-1001', '2341', '$500.00', '1/20/14']
['Supplier X', '001-1001', '2341', '$500.00', '1/20/14']
['Supplier X', '001-1001', '5467', '$750.00', '1/20/14']
['Supplier X', '001-1001', '5467', '$750.00', '1/20/14']
['Supplier Y', '50-9501', '7009', '$250.00', '1/30/14']
['Supplier Y', '50-9501', '7009', '$250.00', '1/30/14']
['Supplier Y', '50-9505', '6650', '$125.00', '2/3/14']
['Supplier Y', '50-9505', '6650', '$125.00', '2/3/14']
['Supplier Z', '920-4803', '3321', '$615.00', '2/3/14']
['Supplier Z', '920-4804', '3321', '$615.00', '2/10/14']
['Supplier Z', '920-4805', '3321', '$615.00', '2/17/14']
['Supplier Z', '920-4806', '3321', '$615.00', '2/24/14']
"""