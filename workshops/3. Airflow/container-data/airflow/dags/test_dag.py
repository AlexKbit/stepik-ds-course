from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator


dag = DAG(dag_id='test-dag-2',
          start_date=datetime(2022, 3, 30),
          max_active_runs = 1,
          schedule_interval='@daily')

t1 = DummyOperator(task_id='task1', dag=dag)
t2 = DummyOperator(task_id='task2', dag=dag)
t3 = DummyOperator(task_id='task3', dag=dag)

t1 >> t2 >> t3
