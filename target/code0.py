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
        # ...y recibe e imprime
        start = MPI.Wtime()
        msg = comm.recv(source=1)
        end = MPI.Wtime()
        print(f"Mensaje recibido de 1: {msg} (tiempo: {end - start:.6f} segundos)")
    elif rank == 1:
        # Los no-root envían su mensaje al root
        start = MPI.Wtime()
        comm.send(message, dest=0)
        end = MPI.Wtime()
        print(f"Proceso {rank} envió su mensaje (tiempo: {end - start:.6f} segundos)")

if __name__ == "__main__":
    main()