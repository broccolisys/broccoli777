import time

now = time.localtime()
main_time= "%02d" % (now.tm_min)

# print(main_time)

while True:
    if main_time == "19":
        print("good")
        break
    else: print("None")