# Jupyterhub

A repository of notebooks to deploy. You will need [docker](https://www.docker.com/) installed on your machine.

## Build

To build the docker image run the following:

```
docker build -t <IMAGE_NAME> <SUBDIRECTORY>
```

There are instructions below for running the notebook. To use the notebook in a production setting you will need to push it to [dockerhub](https://www.docker.com/products/docker-hub):

```
docker push <IMAGE_NAME>
```

## Run locally

Create a `docker.env` file with the following variables

```
DJANGO_ALLOW_ASYNC_UNSAFE=True
DJANGO_SETTINGS_MODULE=api.settings
DJANGO_DATABASE_NAME=<DATABASE>
DJANGO_DATABASE_USER=<USER>
DJANGO_DATABASE_PASSWORD=<PASSWORD>
DJANGO_DATABASE_HOST=<HOST>
```

Then, run the docker image with the environment variables defined

```
docker run -p 8888:8888 --env-file docker.env <notebook>
```

## Notebooks

## Deploy 

To deploy our Jupyterhub configuration onto a Kubernetes cluster we can run

```
helm install jupyterhub jupyterhub/jupyterhub -f config.yml -n jupyter --timeout 500s
```

Alternatively, to update the configuration we can use

```
helm upgrade --cleanup-on-fail jupyterhub jupyterhub/jupyterhub -f config.yml -n jupyter --timeout 180s
```

## Notebooks

### WALLABY Admin

The WALLABY admin notebook is used to maintain the archive. It requires read/write access to the database and will be accessible only by authorised users. 

In the notebook we go through the scenario of developing a detection duplicate matching algorithm, which can be deployed as a RADEC workflow, and re-running `sofia` on detections that have been identified as duplicates.

### WALLABY Science User

**TODO(austin): This notebook requires updating**

The WALLABY science user notebook can be used to explore and perform analysis on the content of the database. It provides read-only access to a view of the database, and some computing resource guarantee.

In the notebook we go through an example science workflow. We perform a filter on the detection table of the database to retreive a subset of interest, plot characteristics of that subset and visualise the products.

### Django Tutorial

The Django tutorial provides a very accessible starting point to users that have never used Django before. Since a comprehensive understanding of the framework is unnecessary for using the ORM, we go through some examples where we construct practically useful queries. This notebook is more verbose and targeted at beginners. Experienced users of `Python` can probably skip this notebook and work directly with one of the aforementioned science notebooks.
