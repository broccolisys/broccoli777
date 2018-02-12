import json
from collections import OrderedDict
from pprint import pprint

with open("jtbcnews_facebook_2018-01-24_2018-01-25.json",encoding="utf-8") as json_data:
    json_data_load = json.load(json_data)
    json_data_string = json.dumps(json_data_load)
    json_big_data = json.loads(json_data_string)

big_data_store = []
for i in range(len(json_big_data["data"])):
    big_data_store.append(json_big_data["data"][i]["shares"]["count"])

big_data = list(set(big_data_store))
big_data_sorted = sorted(big_data,reverse=True)
print(big_data_sorted)
data_store = []

for x in big_data_sorted:
    for i in range(len(big_data_store)):
        try:
            if x == json_big_data["data"][i]["shares"]["count"]:
                print("제목: %s" % json_big_data["data"][i]["name"])
                print("링크: %s" % json_big_data["data"][i]["link"])
                print("공유수: %s" %json_big_data["data"][i]["shares"]["count"])

        except KeyError:
            print("해당 기사는 제목이 없습니다")




