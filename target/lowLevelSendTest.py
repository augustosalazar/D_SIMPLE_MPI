from mpi4py import MPI
import sys
import time
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

dataSize = sys.argv[1] if len(sys.argv) > 1 else 20  # Default 20 elements
dataSize = int(dataSize)

if rank == 0:
    data1 = np.random.rand(dataSize).astype('f')  # float32 array
    print("I am process", rank, "going to send to process 1")
    start = MPI.Wtime()
    comm.Send([data1, MPI.FLOAT], dest=1)
    end = MPI.Wtime()
    print("I am process", rank, "sent data to 1 in", end - start, "seconds")

    data2 = np.random.rand(dataSize).astype('f')
    print("I am process", rank, "going to send to process 2")
    start = MPI.Wtime()
    comm.Send([data2, MPI.FLOAT], dest=2)
    end = MPI.Wtime()
    print("I am process", rank, "sent data to 2 in", end - start, "seconds")

elif rank == 1:
    print("I am process", rank, "going to receive, but first wait 3 seconds")
    time.sleep(3)
    recv_data = np.empty(dataSize, dtype='f')
    start = MPI.Wtime()
    comm.Recv([recv_data, MPI.FLOAT], source=0)
    end = MPI.Wtime()
    print("I am process", rank, "msg received in", end - start, "seconds, data", recv_data[:3])

elif rank == 2:
    print("I am process", rank, "going to receive, but first wait 1 second")
    time.sleep(1)
    recv_data = np.empty(dataSize, dtype='f')
    start = MPI.Wtime()
    comm.Recv([recv_data, MPI.FLOAT], source=0)
    end = MPI.Wtime()
    print("I am process", rank, "msg received in", end - start, "seconds, data", recv_data[:3])
