# Jupyterhub Notebooks

## Run locally

The collection of AusSRC notebooks provided for RADEC users. Users are able to build and run the images locally. The following command is used to run a notebook

```
docker run -p 8888:8888 --env-file env/docker.env <notebook>
```

Note also that the `docker.env` file is used for setting Django the following database environment variables

* `DJANGO_DATABASE_NAME`
* `DJANGO_DATABASE_USER`
* `DJANGO_DATABASE_PASSWORD`
* `DJANGO_DATABASE_HOST`

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

The WALLABY science user notebook can be used to explore and perform analysis on the content of the database. It provides read-only access to a view of the database, and some computing resource guarantee.

In the notebook we go through an example science workflow. We perform a filter on the detection table of the database to retreive a subset of interest, plot characteristics of that subset and visualise the products.

### Django Tutorial

The Django tutorial provides a very accessible starting point to users that have never used Django before. Since a comprehensive understanding of the framework is unnecessary for using the ORM, we go through some examples where we construct practically useful queries. This notebook is more verbose and targeted at beginners. Experienced users of `Python` can probably skip this notebook and work directly with one of the aforementioned science notebooks.
