FROM bitnami/spark:3.3.2-debian-11-r22

USER root
RUN apt-get update && apt-get install -y \
    curl
RUN curl https://jdbc.postgresql.org/download/postgresql-42.2.18.jar -o /opt/bitnami/spark/jars/postgresql-42.2.18.jar