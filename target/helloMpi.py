# hello_mpi.py

from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Cada proceso envía al root (rank 0) su mensaje
    message = f"¡Hola desde el proceso {rank} de {size}!"
    if rank == 0:
        # El root imprime su propio mensaje...
        print(message)
        # ...y recibe e imprime los de los demás
        for src in range(1, size):
            msg = comm.recv(source=src)
            print(msg)
    else:
        # Los no-root envían su mensaje al root
        comm.send(message, dest=0)

if __name__ == "__main__":
    main()