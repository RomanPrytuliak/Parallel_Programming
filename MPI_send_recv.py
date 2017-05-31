from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    value = 777
    comm.send(value, dest = 1)
elif rank == 1:
    value = comm.recv(source = 0)
else:
    value = 0

print("Process #{} got value {}".format(rank, value))