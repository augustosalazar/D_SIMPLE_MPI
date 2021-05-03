FROM python:3
RUN apt update
RUN apt -y install nano
RUN apt -y install sudo
RUN apt -y install libopenmpi-dev
RUN pip install mpi4py
RUN adduser --disabled-password --gecos "" mpirun
RUN echo "mpirun ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN mkdir /app
RUN chown mpirun:mpirun /app