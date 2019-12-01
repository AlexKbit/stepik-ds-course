from datetime import datetime
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator


def load():
    return int(Variable.get('value'))


def multiply(**ctx):
    x = ctx['ti'].xcom_pull(key='return_value', task_ids='load_task')
    x = x * 25
    return x


def plus(**ctx):
    x = ctx['ti'].xcom_pull(key='return_value', task_ids='multiply_task')
    x = x + 5
    return x


def upload(**ctx):
    x = ctx['ti'].xcom_pull(key='return_value', task_ids='plus_task')
    Variable.set('result', x)


dag = DAG(dag_id='calculation-dag',
          start_date=datetime(2019, 11, 30),
          schedule_interval='@once')

load_task = PythonOperator(task_id='load_task',
                           python_callable=load,
                           dag=dag)
multiply_task = PythonOperator(task_id='multiply_task',
                               python_callable=multiply,
                               provide_context=True,
                               dag=dag)
plus_task = PythonOperator(task_id='plus_task',
                           python_callable=plus,
                           provide_context=True,
                           dag=dag)
upload_task = PythonOperator(task_id='upload_task',
                             python_callable=upload,
                             provide_context=True,
                             dag=dag)


load_task >> multiply_task >> plus_task >> upload_task
