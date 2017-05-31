import threading

barrier = threading.Barrier(2)

def function(thread_name):
    print(thread_name + ": A")
    barrier.wait()
    print(thread_name + ": B")

threading.Thread(target = function, args = ("thread_0", )).start()
threading.Thread(target = function, args = ("thread_1", )).start()
