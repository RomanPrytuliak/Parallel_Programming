import time
import numpy as np
from multiprocessing import Process, Manager

def function(counts, lock):
    lock.acquire()
    if counts[0] == 0:
        time.sleep(1)
        counts[0] += 1
    lock.release()
        
processes = []
manager = Manager()
counts = manager.list([0])
lock = manager.Lock()
for i in range(2):
    processes.append(Process(target = function, args = (counts, lock)))
    processes[-1].start()

for process in processes:
    process.join()

print(counts[0])