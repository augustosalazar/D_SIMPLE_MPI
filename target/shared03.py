from mpi4py import MPI
import numpy as np
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size < 3:
    raise ValueError("Este ejemplo requiere al menos 3 procesos")

# Solo rank 0 reserva memoria compartida: 1 valor double
win = MPI.Win.Allocate_shared(8 if rank == 0 else 0, disp_unit=8, comm=comm)
buf, itemsize = win.Shared_query(0)
slot = np.ndarray(buffer=buf, dtype='d', shape=(1,))  # solo un dato

comm.Barrier()

if rank == 0:
    # PRODUCTOR
    for i in range(5):
        valor = random.random()
        # Espera a obtener el lock antes de escribir
        win.Lock(rank=0)
        slot[0] = valor
        win.Unlock(rank=0)
        print(f"[Productor] Escribió: {valor:.4f}")
        time.sleep(1.0)

    # Señal de terminación
    win.Lock(rank=0)
    slot[0] = -1.0
    win.Unlock(rank=0)

else:
    # CONSUMIDOR
    while True:
        # Intenta leer protegidamente
        win.Lock(rank=0)
        valor = slot[0]
        win.Unlock(rank=0)

        if valor < 0:
            print(f"[Consumidor {rank}] Terminando")
            break

        print(f"[Consumidor {rank}] Leyó: {valor:.4f}")
        time.sleep(1.5)
