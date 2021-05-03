from mpi4py import MPI
import time
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
if rank == 0:
	data = [1,2,3]
	print ("I am process ",rank,"... going to send")
	comm.isend(data, dest=1)
	data = [4,5,6]
	comm.isend(data, dest=2)
	print("I am process ",rank,"sent")
elif rank == 1:
	data = []
	print ("I am process ",rank,"... going to receive, but first wait 3 seconds")
	time.sleep(3)
	data = comm.recv(source=0)
	print ("I am process ",rank,"... msg received ", data)
elif rank == 2:
	data = []
	print ("I am process ",rank,"... going to receive, but first wait 1 seconds")
	time.sleep(1)
	data = comm.recv(source=0)
	print ("I am process ",rank,"... msg received ", data)
