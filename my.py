from multiprocessing import Process
import sys
from time import sleep

def func(name):
    print(f"start {name}")
    sleep(3)
    print(f"finish {name}")
    sys.exit(0)

proc1 = Process(target=func, args=(1,))
proc2 = Process(target=func, args=(2,))
proc3 = Process(target=func, args=(3,))

proc1.start()
proc2.start()
proc3.start()

proc1.join()
proc2.join()
proc3.join()
