from threading import Thread

def function():
    while True:
        pass

threads = []
for i in range(20):
    threads.append(Thread(target = function))
    threads[-1].start()
