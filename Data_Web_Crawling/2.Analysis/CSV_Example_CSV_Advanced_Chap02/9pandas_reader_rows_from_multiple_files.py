"""2.10 여러 파일의 데이터 합치기-pandas
유사한 데이터가 들어 있는 여러 개의 파일이 있는 경우 모든 데이터를 하나의 파일에 포함되도록
합쳐야 할때

기본 프로세스는 각 입력 파일을 data_frame 으로 읽어 드리고
all_data_frame 리스트에 추가한 다음
concat() 함수를 사용하여 모든 데이터 프레임을 하나의 데이터 프레임으로 합친다
(concat() 함수는 axis 인수를 통해서 데이터 프레임을 병합하는 방향을 수직(axis=0) 또는 수평(axis=1)로 지정할수있다.
"""

import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path, 'sales_*'))

all_data_frames = []
for file in all_files:
    data_frame = pd.read_csv(file, index_col=None)
    # index_col : 테이블 내의 특정한 열을 행 인덱스로 지정하고 싶을때
    # 만약 index_col = ss 라고 하면 행 index에 ss가 들어간다.
    all_data_frames.append(data_frame)
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index = False)
