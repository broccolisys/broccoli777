import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name='january_2013')
# sheet 이름이 'january_2013'의 data를 가져와서 data_frame에 할당
writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name = 'jan_13_output', index=False)
# data_frame의 내용을 output_file 이름을 가진 ExcelWriter의 객체의 sheet 이름이 jan_13_output 라는 excel 에 넣음
writer.save()
# 저장

"""
Notes

If passing an existing ExcelWriter object, then the sheet will be added to the existing workbook. 
This can be used to save different DataFrames to one workbook:

>>> writer = pd.ExcelWriter('output.xlsx')
>>> df1.to_excel(writer,'Sheet1')
>>> df2.to_excel(writer,'Sheet2')
>>> writer.save()
For compatibility with to_csv, to_excel serializes(직렬화하다) lists and dicts to strings before writing.
: to_csv 와는 달리 to_excel은 저장되기전에 list와 dict을 string 형태로 직렬화 시켜야함
"""