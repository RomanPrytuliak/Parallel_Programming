import time
import threading

count = 0
lock = threading.Lock()

def function():
    global count
    lock.acquire()
    if count == 0:
        time.sleep(1)
        count += 1
        lock.release()

threads = []
for i in range(3):
    threads.append(threading.Thread(target = function))
    threads[-1].start()

for thread in threads:
    thread.join()

print(count)