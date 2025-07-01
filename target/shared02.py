from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print(f"Proceso {rank} de {size} iniciado.")

# Crear una ventana de memoria compartida entre procesos en el mismo nodo
win = MPI.Win.Allocate_shared(
    size=4 * size if rank == 0 else 0,  # Solo el rank 0 reserva memoria
    disp_unit=4,
    comm=comm
)

# Todos obtienen acceso al mismo bloque compartido
buf, itemsize = win.Shared_query(0)
assert itemsize == 4
array = np.ndarray(buffer=buf, dtype='i', shape=(size,))

# Sincronizar
comm.Barrier()

# Cada proceso escribe en su posición
array[rank] = rank * 10

# Esperar a que todos escriban
comm.Barrier()

if rank == 0:
    print("Contenido del array compartido:")
    print(array)
