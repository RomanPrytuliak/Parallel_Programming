from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = [x ** 2 for x in range(size)]
else:
    data = None

data = comm.bcast(data, root = 0)
# Now every process has the data...
data_piece = comm.scatter(data, root = 0)
# ...as well as its dedicated task

assert data == [x ** 2 for x in range(size)]
print("Process #{} got {}".format(rank, data_piece))