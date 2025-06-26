# Simple MPI sample using Docker

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
docker run --rm -v "%cd%\target:/app" augustosalazar/un_mpi_image:v5 mpiexec --allow-run-as-root -n 2 python /app/code0.py
¡Hola desde el proceso 0 de 2!
Mensaje recibido de 1: ¡Hola desde el proceso 1 de 2! (tiempo: 0.000504 segundos)
Proceso 1 envió su mensaje (tiempo: 0.000045 segundos)
```

```bash
docker run --rm -v "%cd%\target:/app" augustosalazar/un_mpi_image:v5 mpiexec --allow-run-as-root -n 6 python /app/code0.py
¡Hola desde el proceso 0 de 6!
Mensaje recibido de 1: ¡Hola desde el proceso 1 de 6! (tiempo: 0.000939 segundos)
Proceso 1 envió su mensaje (tiempo: 0.000067 segundos)
```

## code1.py

It shows how to send messages between processes using MPI with multiple nodes.

```bash
docker run --rm -v "%cd%\target:/app" augustosalazar/un_mpi_image:v5 mpiexec --allow-run-as-root -n 6 python /app/code1.py
¡Hola desde el proceso 0 de 6!
Proceso 1 envió su mensaje (tiempo: 0.000300 segundos)
Proceso 2 envió su mensaje (tiempo: 0.000261 segundos)
Proceso 3 envió su mensaje (tiempo: 0.000318 segundos)
Proceso 4 envió su mensaje (tiempo: 0.000336 segundos)
Proceso 5 envió su mensaje (tiempo: 0.000324 segundos)
Mensaje recibido de 1: ¡Hola desde el proceso 1 de 6! (tiempo: 0.001264 segundos)
Mensaje recibido de 2: ¡Hola desde el proceso 2 de 6! (tiempo: 0.000012 segundos)
Mensaje recibido de 3: ¡Hola desde el proceso 3 de 6! (tiempo: 0.000008 segundos)
Mensaje recibido de 4: ¡Hola desde el proceso 4 de 6! (tiempo: 0.000006 segundos)
Mensaje recibido de 5: ¡Hola desde el proceso 5 de 6! (tiempo: 0.000006 segundos)
```

## sendtest.py

```bash
docker run --rm -v "%cd%\target:/app" augustosalazar/un_mpi_image:v5 mpiexec --allow-run-as-root -n 3 python /app/sendtest.py
I am process  0  going to send
I am process  1  going to receive, but first wait 3 seconds
I am process  2  going to receive, but first wait 1 seconds
I am process  0  sent data to 1 in  0.0002491  seconds
I am process  0  sent data to 2 in  4.600000000000003e-06  seconds
I am process  2  msg received in  0.0015265  seconds, data [0.6429036524183926, 0.9811815650821261, 0.8000203378671583]
I am process  1  msg received in  8.56e-05  seconds, data [0.22994304284939338, 0.44943814413441063, 0.6145883308445463]
```

```bash
docker run --rm -v "%cd%\target:/app" augustosalazar/un_mpi_image:v5 mpiexec --allow-run-as-root -n 3 python /app/sendtest.py 40000
I am process  1  going to receive, but first wait 3 seconds
I am process  0  going to send
I am process  2  going to receive, but first wait 1 seconds
I am process  0  sent data to 1 in  3.0025017  seconds
I am process  1  msg received in  0.0017832  seconds, data [0.2863977651541396, 0.19195655096407283, 0.9102918770372733]
I am process  0  sent data to 2 in  0.0015640000000001208  seconds
I am process  2  msg received in  2.0043185  seconds, data [0.8867952239532707, 0.07933763012857642, 0.8283312684907489]
```

```bash
docker run --rm -v "%cd%\target:/app" augustosalazar/un_mpi_image:v5 mpiexec --allow-run-as-root -n 3 python /app/lowLevelSendTest.py
I am process 1 going to receive, but first wait 3 seconds
I am process 2 going to receive, but first wait 1 second
I am process 0 going to send to process 1
I am process 0 sent data to 1 in 0.0006469 seconds
I am process 0 going to send to process 2
I am process 0 sent data to 2 in 6.200000000000042e-06 seconds
I am process 2 msg received in 8.31e-05 seconds, data [0.8370235 0.661478  0.6755458]
I am process 1 msg received in 4.93e-05 seconds, data [0.09237162 0.6890432  0.9405974 ]
```

```bash
docker run --rm -v "%cd%\target:/app" augustosalazar/un_mpi_image:v5 mpiexec --allow-run-as-root -n 3 python /app/lowLevelSendTest.py 40000
I am process 2 going to receive, but first wait 1 second
I am process 0 going to send to process 1
I am process 1 going to receive, but first wait 3 seconds
I am process 0 sent data to 1 in 3.001487 seconds
I am process 1 msg received in 0.0001234 seconds, data [0.00958399 0.9023033  0.9253317 ]
I am process 0 going to send to process 2
I am process 0 sent data to 2 in 9.10000000002853e-05 seconds
I am process 2 msg received in 2.0005069 seconds, data [0.62247777 0.0890263  0.17499022]
```

### Activities

Find the differences and preferred scenario of the following methods in MPI: send, ssend, isend, Send, Ssend, ISend, recv, irecv, Recv and IRecv.