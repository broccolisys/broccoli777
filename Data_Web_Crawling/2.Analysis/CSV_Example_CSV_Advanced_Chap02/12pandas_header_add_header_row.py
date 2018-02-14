"""2.8 헤더 추가하기-pandas
가끔씩 헤더 행이 포함되지 않는 경우가 종종 있다. 이럴때 파이썬 스크립트를 이용해 열 헤더를 추가할 수 있다.
"""

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

header_list = ['Supplier Name', 'Invoice Number',\
                       'Part Number', 'Cost', 'Purchase Date']

data_frame = pd.read_csv(input_file, header=None, names = header_list)

data_frame.to_csv(output_file, index=False)
