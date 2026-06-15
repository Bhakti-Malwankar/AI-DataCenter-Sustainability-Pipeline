from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "bhakti",
}

with DAG(
    dag_id="ai_datacenter_pipeline",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    extract_task = BashOperator(
        task_id="extract_data",
        bash_command="python etl/extract.py",
    )

    transform_task = BashOperator(
        task_id="transform_data",
        bash_command="python etl/transform.py",
    )

    load_task = BashOperator(
        task_id="load_data",
        bash_command="python etl/load.py",
    )

    report_task = BashOperator(
        task_id="generate_report",
        bash_command="python reports/generate_report.py",
    )

    extract_task >> transform_task >> load_task >> report_task