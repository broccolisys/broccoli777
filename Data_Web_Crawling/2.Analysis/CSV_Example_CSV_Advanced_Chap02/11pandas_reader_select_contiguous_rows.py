"""연속된 행 선택하기-pandas
행의 인덱스 값 또는 열 헤더를 기반으로 행 또는 열을 삭제하기 위한 drop() 함수를 이용
"""
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file, header=None)

data_frame = data_frame.drop([0,1,2,16,17,18])
data_frame.columns = data_frame.iloc[0]
data_frame = data_frame.reindex(data_frame.index.drop(3))
#reindex() : 하나 이상의 축을 새로운 인덱스에 맞출수 있게 해줌

"""ps : read_csv 함수에 header=None 을 지정하여 기본값인 1행을 헤더로 읽는 것을 막았고, 불필요한 행을 삭제
한 다음에는 데이터가 시작되는 0행을 열 헤더로 시작됐다. 그 다음 reindex로 행 인덱스를 다시 지정했다. 인덱스 리스트에서 
3을 뺀것은, 3은 헤더행의 인덱스이므로, 데이터 인덱스에서 제외되어야 하기 때문이다. 이렇게 인덱스를 다시
지정하지 않으면 인덱스가 3인 열 헤더행까지 데이터에 포함되므로, 출력 파일에 헤더행이 두번 들어가게 된다"""

data_frame.to_csv(output_file, index=False)
