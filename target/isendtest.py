from mpi4py import MPI
import sys
import random
import time
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

dataSize = sys.argv[1] if len(sys.argv) > 1 else 20 # 20 is default
dataSize = int(dataSize)

if rank == 0:
	data = [random.random() for _ in range(dataSize)]   # 1.28 MB
	print ("I am process ",rank," going to send")
	start = MPI.Wtime()
	comm.isend(data, dest=1)
	end = MPI.Wtime()
	print("I am process ",rank," sent data to 1 in ", end-start, " seconds")
	data = [random.random() for _ in range(dataSize)]  #  1.28 MB
	start = MPI.Wtime()
	comm.isend(data, dest=2)
	end = MPI.Wtime()
	print("I am process ",rank," sent data to 2 in ", end-start, " seconds")
elif rank == 1:
	data = []
	print ("I am process ",rank," going to receive, but first wait 3 seconds")
	time.sleep(3)
	start = MPI.Wtime()
	data = comm.recv(source=0)
	end = MPI.Wtime()
	print("I am process ",rank," msg received in ", end-start, " seconds, data", data[:3])
elif rank == 2:
	data = []
	print ("I am process ",rank," going to receive, but first wait 1 seconds")
	time.sleep(1)
	start = MPI.Wtime()
	data = comm.recv(source=0)
	end = MPI.Wtime()
	print ("I am process ",rank," msg received in ", end-start, " seconds, data",data[:3] )
