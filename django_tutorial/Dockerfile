FROM jupyter/base-notebook
WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN rm requirements.txt

# Note: --chown=jovyan is to allow user access to local sqlite database.
COPY --chown=jovyan . ./src/
COPY ./notebook.ipynb .
