docker run -d -it --name mpicont -v "%cd%\target:/app" augustosalazar/un_mpi_image:v5

docker run -d -it --name mpicont -v "$(pwd)"/target:/app augustosalazar/un_mpi_image:v5

docker exec -it mpicont mpiexec --allow-run-as-root -n 3 python /app/sendtest.py

To install nano on Play with Docker:
apk --update add nano


docker run --rm -v "%cd%\target:/app" augustosalazar/un_mpi_image:v5 mpiexec --allow-run-as-root -n 3 python /app/helloMpi.py

docker run --rm -v "$(pwd)"/target:/app augustosalazar/un_mpi_image:v5 mpiexec --allow-run-as-root -n 3 python /app/helloMpi.py