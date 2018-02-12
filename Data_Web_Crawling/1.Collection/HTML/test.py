import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from matplotlib import style

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
style.use('ggplot')

ebiga_csv = "Ebiga_store_BigData.csv"
with open(ebiga_csv,"r") as infile:
    data = list(csv.reader(infile))


def get_address_info():
    data_store = []
    for i in range(1, int(len(data))):
        address = data[i][2]
        data_store.append(address)
        i += 1
    return data_store

def get_canvas_info():
    canvas_store = []
    for canvas in get_address_info():
        canvas_data = canvas.split()
        canvas_store.append(canvas_data[0])
    canvas_str = str("/".join(canvas_store))
    canvas_str = canvas_str.replace('강서구','서울특별시')
    canvas_str = canvas_str.replace('서울특별시','서울')
    canvas_str = canvas_str.replace('서울시', '서울')
    canvas_str = canvas_str.replace('광주시', '광주')
    canvas_str = canvas_str.replace('전라남도','전남')
    canvas_str = canvas_str.replace('인천광역시','인천')
    canvas_str = canvas_str.replace('대구광역시','대구')
    canvas_str = canvas_str.replace('부산광역시','부산')
    canvas_str = canvas_str.replace('충청북도','충북')
    canvas_str = canvas_str.replace('충청남도','충남')
    canvas_str = canvas_str.replace('경기도','경기')
    canvas_str = canvas_str.replace('경상북도','경북')
    canvas_str = canvas_str.replace('경상남도','경남')
    canvas_str = canvas_str.replace('제주특별자치도', '제주')
    canvas_list = canvas_str.split("/")
    return canvas_list

result1 = []
result2 = []

for city in set(get_canvas_info()):
    result1.append(city)
    result2.append(get_canvas_info().count(city))


fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

ypos = np.arange(17)
rects = plt.barh(ypos, result2, align='center', height=0.5)
plt.yticks(ypos, result1)

for i, rect in enumerate(rects):
    ax.text(0.95 * rect.get_width(), rect.get_y() + rect.get_height() / 2.0, str(result2[i]) + '개', ha='right', va='center')

plt.xlabel('지점 갯수')
plt.show()

# pos = np.arange(17)
# rects = plt.bar(pos, result2, align='center', width=0.5)
# plt.xticks(pos, result1)
#
# for i, rect in enumerate(rects):
#     ax.text(rect.get_x() + rect.get_width() / 2.0, 0.95 * rect.get_height(), str(result2[i]) + '%', ha='center')
#
# plt.ylabel('지점갯수')
