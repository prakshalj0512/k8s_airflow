import airflow
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def print_hello():
    return ('Hello world!')


args = {
    'owner': 'airflow',
    'email': ['example@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(seconds=60)
}
dag = DAG(
    dag_id='hello_world', default_args=args,
    schedule_interval=None)


bash_operator = BashOperator(
    task_id='bash_task', bash_command="echo 1", retries=1, dag=dag)
hello_operator = PythonOperator(
    task_id='hello_task', python_callable=print_hello, dag=dag)


bash_operator >> hello_operator

