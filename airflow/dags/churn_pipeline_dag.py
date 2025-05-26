from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'bharat',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='customer_churn_pipeline',
    default_args=default_args,
    description='ELT pipeline for customer churn data',
    schedule_interval='@hourly',
    start_date=datetime(2023, 1, 1),
    catchup=False
)

transform_task = BashOperator(
    task_id='transform_data',
    bash_command='python /opt/airflow/etl/transform.py',
    dag=dag,
)

load_task = BashOperator(
    task_id='load_to_sqlserver',
    bash_command='python /opt/airflow/etl/load_to_sqlserver.py',
    dag=dag,
)

transform_task >> load_task
