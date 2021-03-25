FROM jupyter/base-notebook
WORKDIR /app

# TODO(austin): replace this with git clone when you figure it out.
COPY SoFiAX_services SoFiAX_services
RUN pip install -r SoFiAX_services/api/requirements.txt

COPY ./notebooks/ .