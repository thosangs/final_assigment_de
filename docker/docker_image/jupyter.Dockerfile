FROM jupyter/pyspark-notebook:spark-3.3.2
USER root

RUN apt-get update && apt-get install -y \
    curl
RUN curl https://jdbc.postgresql.org/download/postgresql-42.2.18.jar -o /opt/postgresql-42.2.18.jar
COPY ./requirements.txt /opt/app/requirements.txt
RUN pip install -r /opt/app/requirements.txt --no-cache-dir