from mpi4py import MPI
import numpy as np
import math
import time

def es_primo(n):
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Lista de números de 4 dígitos
numeros = np.arange(1000, 10000, dtype='i')
total = len(numeros)

# Proceso 0 reserva memoria para todos los números
win = MPI.Win.Allocate_shared(
    numeros.nbytes if rank == 0 else 0,
    disp_unit=numeros.itemsize,
    comm=comm
)

# Todos acceden a la memoria compartida
buf, itemsize = win.Shared_query(0)
array = np.ndarray(buffer=buf, dtype='i', shape=(total,))

comm.Barrier()

# Solo el proceso 0 inicializa la matriz
if rank == 0:
    array[:] = numeros

comm.Barrier()

# Todos los procesos trabajan en paralelo
while True:
    encontrado = False
    for i in range(rank, total, size):
        win.Lock(rank=0)
        val = array[i]
        if val > 0:
            array[i] = -1  # marcar como en revisión
            win.Unlock(rank=0)

            # Verificar si es primo
            primo = es_primo(val)

            win.Lock(rank=0)
            array[i] = 1 if primo else 0
            win.Unlock(rank=0)

            encontrado = True
        else:
            win.Unlock(rank=0)
    # Si nadie encontró nada en esta ronda, se termina
    all_done = comm.allreduce(encontrado, op=MPI.LOR)
    if not all_done:
        break

comm.Barrier()

# El proceso 0 cuenta cuántos primos encontró
if rank == 0:
    cantidad_primos = np.count_nonzero(array == 1)
    print(f"Total de primos de 4 dígitos encontrados: {cantidad_primos}")
