"""CSV파일 읽고 쓰기-pandas"""

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
# list, dictionary, tuple 과 같이 data_frame 형식 또한 데이터를 저장하는 한 방식
# 대신 data를 '표'형태로 만들어 저장
print(data_frame)
data_frame.to_csv(output_file, index=False)
