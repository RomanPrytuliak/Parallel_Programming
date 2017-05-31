import time
import numpy as np
import sharedmem
from multiprocessing import Process, Manager

def function(counts, lock):
    with lock:
        if counts[0]['foo'] == 0:
            time.sleep(1)
            counts[0]['foo'] += 1
        
processes = []
manager = Manager()
counts = sharedmem.full(1, (0, ), dtype = [('foo', 'i1')])
lock = manager.Lock()
for i in range(2):
    processes.append(Process(target = function, args = (counts, lock)))
    processes[-1].start()

for process in processes:
    process.join()

print(counts[0]['foo'])