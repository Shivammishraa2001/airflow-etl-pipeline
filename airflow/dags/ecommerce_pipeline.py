from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(
    dag_id="ecommerce_etl_pipeline",
    start_date=datetime(2026,1,1),
    schedule="@daily",
    catchup=False
) as dag:


    generate_data=BashOperator(
        task_id="generate_data",
        bash_command="python /opt/airflow/src/generate_data.py"
    )


    transform_data=BashOperator(
        task_id="transform_data",
        bash_command="python /opt/airflow/src/transform.py"
    )


    load_data=BashOperator(
        task_id="load_data",
        bash_command="python /opt/airflow/src/load.py"
    )


    generate_data >> transform_data >> load_data