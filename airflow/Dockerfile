FROM apache/airflow:2.6.3

USER root
RUN apt-get update && \
    apt-get install -y gcc g++ gnupg curl unixodbc-dev wget apt-transport-https

# SQL Server ODBC driver
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

USER airflow
COPY ./etl /opt/airflow/etl
COPY ./data /opt/airflow/data
