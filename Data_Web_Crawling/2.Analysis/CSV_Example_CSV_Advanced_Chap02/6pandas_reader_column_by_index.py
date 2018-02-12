"""특정열(column) 선택하기
열의 인덱스 값을 사용하여 특정 열을 선택하는 방법-pandas"""
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_column_by_index = data_frame.iloc[:,[0,3]]
# iloc를 이용하여 index value 기반으로 column 선택( iloc = integer location)
data_frame_column_by_index.to_csv(output_file, index =False)
