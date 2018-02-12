import sched, time
s = sched.scheduler(time.time, time.sleep)

data = "저장완료"
def saving_time():
    print("saving")

def saved_time():
    print("saved")

def print_some_times():
    while True:
        s.enter(1, 1, saving_time)
        with open("goods.txt", 'w') as data:
            data.write('good')
        s.enter(10, 1, saved_time)
        s.run()

print_some_times()
p
# def do_something():
#     print("저장합니다")
#
#     s.enter(10, 1, do_something)
#     s.run()
#     print('good')
#
# do_something()