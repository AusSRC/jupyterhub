FROM jupyter/base-notebook
WORKDIR /app

# install git
USER root
RUN apt-get update && apt-get install -y git build-essential wcslib-dev
RUN apt install -y libomp-dev

# clone repositories
RUN git clone https://github.com/axshen/SoFiAX_services.git &&\
    git clone https://github.com/AusSRC/SoFiAX.git &&\
    git clone https://github.com/SoFiA-Admin/SoFiA-2.git

# build SoFiA-2
RUN cd SoFiA-2 && ./compile.sh -fopenmp
RUN cd SoFiA-2 && mv sofia /usr/local/bin/

# build SoFiA-X
RUN cd SoFiAX && python -m venv venv && source venv/bin/activate
RUN cd SoFiAX && python setup.py install

# SoFiA-X services
USER jovyan
RUN pip install -r SoFiAX_services/api/requirements.txt
COPY sofia.par sofia.par
COPY ./notebooks/ .