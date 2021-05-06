import sys
from mpi4py import MPI
comm = MPI.COMM_WORLD   # Defines the default communicator
num_procs = comm.Get_size()  # Stores the number of processes in num_procs.
rank = comm.Get_rank()  # Stores the rank (pid) of the current process
if rank == 0:
    print("I am root, have to distribute",sys.argv[1], "numbers")
else:
    print("I am rank",rank, "and I am waiting for my first package")
