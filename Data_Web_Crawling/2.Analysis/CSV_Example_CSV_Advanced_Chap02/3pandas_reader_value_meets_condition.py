"""
특정 조건을 충족하는 행의 필터링-pandas
loc() 이용
쉼표를 기준으로 앞에는 row(행) 필터링 조건
뒤에는 column(열) 필터링 조건
"""

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']\
    .str.contains('Z')) | (data_frame['Cost'] > 600.0), :]
    # row에서 data_frame['Suplier Name']에서 Z를 포함하는 것 or
    # data_Frame['Cost'] 가 600이상인것을 뽑아냄
data_frame_value_meets_condition.to_csv(output_file, index=False)
# csv 파일로 저장장
# \ 역슬래쉬는 한줄의 코드를 두줄로 나누기 위해