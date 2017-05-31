from multiprocessing import Process

def function():
    while True:
        pass

processes = []
for i in range(20):
    processes.append(Process(target = function))
    processes[-1].start()