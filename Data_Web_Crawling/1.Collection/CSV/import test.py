import csv # csv 파일을 불러오기 위한 모듈
import os

print(os.getcwd())
# with open('Demographic_Statistics_By_Zip_Code.csv', newline='') as infile:
#     data = list(csv.reader(infile))
#
# countParticipantsIndex = data[0].index("COUNT PARTICIPANTS")
# print("The index of 'COUNT PARTICIPATNS': " +str(countParticipantsIndex))
#
# countParticipants = []
#
# for row in data[1:]:
#     countParticipants.append(int(row[countParticipantsIndex]))
#
# with open('Demographic_Statistics_By_Zip_Code.csv', newline='') as infile2:
#     data = list(csv.reader(infile2))
#
# countParticipantsIndex2 = data[0].index("COUNT CITIZEN STATUS TOTAL")
# print("The index of 'COUNT CITIZEN STATUS TOTAL' : " + str(countParticipantsIndex2))
#
# countParticipants2 = []
# for row2 in data[1:]:
#     countParticipants2.append(int(row2[countParticipantsIndex2]))
# for matter in countParticipants2:
#     print(matter)

with open('Demographic_Statistics_By_Zip_Code.csv', newline='') as infile2:
    data = list(csv.reader(infile2))

countParticipantsIndex2 = data[0].index("COUNT FEMALE")
print("The index of 'COUNT FEMALE' : " + str(countParticipantsIndex2))

countParticipants2 = []
for row2 in data[1:]:
    countParticipants2.append(int(row2[countParticipantsIndex2]))
for matter in countParticipants2:
    print(matter)