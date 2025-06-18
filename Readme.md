docker run -d -it --name mpicont -v "%cd%\target:/app" augustosalazar/un_mpi_image:v5

docker run -d -it --name mpicont -v "$(pwd)"/target:/app augustosalazar/un_mpi_image:v5

docker exec -it mpicont mpiexec --allow-run-as-root -n 3 python /app/sendtest.py

To install nano on Play with Docker:
apk --update add nano

To run use on the the following commands:

```bash
docker run --rm -v "%cd%\target:/app" augustosalazar/un_mpi_image:v5 mpiexec --allow-run-as-root -n 3 python /app/code0.py
```

```bash
docker run --rm -v "$(pwd)"/target:/app augustosalazar/un_mpi_image:v5 mpiexec --allow-run-as-root -n 3 python /app/code0.py
```

## code0.py

It shows how to send messages between processes using MPI with two nodes.

```bash
C:\desarrollo\D_SIMPLE_MPI>docker run --rm -v "%cd%\target:/app" augustosalazar/un_mpi_image:v5 mpiexec --allow-run-as-root -n 2 python /app/code0.py
¡Hola desde el proceso 0 de 2!
Mensaje recibido de 1: ¡Hola desde el proceso 1 de 2! (tiempo: 0.000504 segundos)
Proceso 1 envió su mensaje (tiempo: 0.000045 segundos)
```

```bash
C:\desarrollo\D_SIMPLE_MPI>docker run --rm -v "%cd%\target:/app" augustosalazar/un_mpi_image:v5 mpiexec --allow-run-as-root -n 6 python /app/code0.py
¡Hola desde el proceso 0 de 6!
Mensaje recibido de 1: ¡Hola desde el proceso 1 de 6! (tiempo: 0.000939 segundos)
Proceso 1 envió su mensaje (tiempo: 0.000067 segundos)
```



