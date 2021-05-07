FROM jupyter/base-notebook
WORKDIR /app

# install git
USER root
RUN apt update && \
    apt install -y libgl1-mesa-glx
RUN apt-get update && \
    apt-get install -y git build-essential wcslib-dev libomp-dev libglib2.0-0 libsm6 libxrender1 libxext6

# clone repositories
RUN git clone https://github.com/AusSRC/SoFiAX_services.git && \
    git clone https://github.com/AusSRC/SoFiAX.git && \
    git clone https://github.com/SoFiA-Admin/SoFiA-2.git

# build SoFiA-2 and SoFiAX
RUN cd SoFiA-2 && \
    ./compile.sh -fopenmp && \
    mv sofia /usr/local/bin/
RUN cd SoFiAX && \
    python3 setup.py install

# SoFiA-X services
USER jovyan
RUN pip3 install -r /app/SoFiAX_services/api/requirements.txt && \
    pip3 install jupyterlab
COPY sofia.par sofia.par
COPY ./notebooks/ .

# workspace
WORKDIR /home/jovyan/