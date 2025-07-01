from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Solo el proceso con rank 0 reserva memoria para el arreglo (8 bytes por double)
win = MPI.Win.Allocate_shared(
    size=8 * size if rank == 0 else 0,
    disp_unit=8,
    comm=comm
)

# Todos los procesos consultan el bloque de memoria compartida
buf, itemsize = win.Shared_query(0)
assert itemsize == MPI.DOUBLE.Get_size()
ary = np.ndarray(buffer=buf, dtype='d', shape=(size,))

# El proceso con rank 1 escribe valores
if rank == 1: 
    ary[:5] = np.arange(5)

# Esperar en el proceso con rank 0 hasta que el proceso 1 haya escrito en el arreglo
comm.Barrier()

# Verificar que el arreglo realmente es compartido y que el proceso 0 puede ver
# los cambios hechos en el arreglo por el proceso 1
if rank == 0:
    print(f"Rank 0 ve ary[:10] =", ary[:10])
