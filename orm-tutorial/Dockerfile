FROM jupyter/base-notebook
WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN rm requirements.txt

COPY . ./src/
COPY ./tutorial.ipynb .