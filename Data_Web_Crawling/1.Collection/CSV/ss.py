with open(file_address, newline='') as infile2:
    data2 = list(csv.reader(infile2))

    countParticipantsIndex2 = data2[0].index(col_instance)
    countParticipants = []
    matters = ''
    for row in data[1:]:
        countParticipants.append(str(row[countParticipantsIndex]))
    for matter in countParticipants:
        matters += matter + '\n'
    return matters