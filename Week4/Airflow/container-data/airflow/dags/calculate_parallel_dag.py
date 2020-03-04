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


def plus5(**ctx):
    x = ctx['ti'].xcom_pull(key='return_value', task_ids='multiply_task')
    x = x + 5
    return x


def plus10(**ctx):
    x = ctx['ti'].xcom_pull(key='return_value', task_ids='multiply_task')
    x = x + 10
    return x


def upload1(**ctx):
    x = ctx['ti'].xcom_pull(key='return_value', task_ids='plus5_task')
    Variable.set('result1', x)


def upload2(**ctx):
    x = ctx['ti'].xcom_pull(key='return_value', task_ids='plus10_task')
    Variable.set('result2', x)


dag = DAG(dag_id='calculation-parallel-dag',
          start_date=datetime(2020, 3, 10),
          schedule_interval='@once')

load_task = PythonOperator(task_id='load_task',
                           python_callable=load,
                           dag=dag)
multiply_task = PythonOperator(task_id='multiply_task',
                               python_callable=multiply,
                               provide_context=True,
                               dag=dag)
plus5_task = PythonOperator(task_id='plus5_task',
                            python_callable=plus5,
                            provide_context=True,
                            dag=dag)
plus10_task = PythonOperator(task_id='plus10_task',
                             python_callable=plus10,
                             provide_context=True,
                             dag=dag)
upload1_task = PythonOperator(task_id='upload1_task',
                              python_callable=upload1,
                              provide_context=True,
                              dag=dag)
upload2_task = PythonOperator(task_id='upload2_task',
                              python_callable=upload2,
                              provide_context=True,
                              dag=dag)


load_task >> multiply_task
multiply_task >> plus5_task >> upload1_task
multiply_task >> plus10_task >> upload2_task
