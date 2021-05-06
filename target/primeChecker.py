import sys
from mpi4py import MPI
comm = MPI.COMM_WORLD   # Defines the default communicator
num_procs = comm.Get_size()  # Stores the number of processes in num_procs.
rank = comm.Get_rank()  # Stores the rank (pid) of the current process


#at the end
if rank == 0:
    print("Number of primer numbers in",sys.argv[1],"is",9999)
    print("Total time",222)
else:
    print("I am rank",rank, "I got",888,"packages")