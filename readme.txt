docker build --tag mpi_image .

docker run -d -it --name mpicont -v "$(pwd)"/target:/app mpi_image

docker exec -it mpicont mpiexec --allow-run-as-root -n 3 python /app/sendtest.py