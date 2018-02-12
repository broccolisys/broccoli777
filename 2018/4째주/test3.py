import threading
from time import sleep

def myThread(name,nsec):
    print ("---- do somthing ----")
    sleep(nsec)

if __name__ == '__main__' :
    t = threading.Thread(target=myThread, args=("Thread-1", 3))
    t.start()
    t.join()
    print ("---- exit ----")


