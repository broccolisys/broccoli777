"""패턴/정규 표현식을 활용한 필터링-pandas
.iloc
integer positon를 통해 값을 찾을 수 있다.
label로는 찾을 수 없다

.loc
label 을 통해 값을 찾을 수 있다.
integer position로는 찾을 수 없다.

.ix
integer position과 label모두 사용 할 수 있다.
만약 label이 숫자라면 label-based index만 된다.

"""

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.ix[data_frame['Invoice Number']\
    .str.startswith("001-"),:]
data_frame_value_matches_pattern.to_csv(output_file, index=False)