from multiprocessing import Pool

def function(x):
    return x * x

pool = Pool(processes = 3)

arguments = [0, 1, 2, 3, 4]
results = pool.map(function, arguments)

print(results) # [0, 1, 4, 9, 16]