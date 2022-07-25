from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator


dag = DAG(dag_id='dummy-dag',
          start_date=datetime(2020, 3, 30),
          schedule_interval='@once')

t1 = DummyOperator(task_id='task1', dag=dag)
t2 = DummyOperator(task_id='task2', dag=dag)
t3 = DummyOperator(task_id='task3', dag=dag)
t4 = DummyOperator(task_id='task4', dag=dag)
t5 = DummyOperator(task_id='task5', dag=dag)
t6 = DummyOperator(task_id='task6', dag=dag)
t7 = DummyOperator(task_id='task7', dag=dag)
t8 = DummyOperator(task_id='task8', dag=dag)
t9 = DummyOperator(task_id='task9', dag=dag)
t10 = DummyOperator(task_id='task10', dag=dag)
t11 = DummyOperator(task_id='task11', dag=dag)
t12 = DummyOperator(task_id='task12', dag=dag)
t13 = DummyOperator(task_id='task13', dag=dag)
t14 = DummyOperator(task_id='task14', dag=dag)
t15 = DummyOperator(task_id='task15', dag=dag)

t1 >> t2
t2 >> t3 >> t5 >> t7
t2 >> t4 >> t6 >> t7
t2 >> t8 >> t7
t2 >> t9 >> t7
t7 >> t10
t10 >> t11 >> t15
t10 >> t12 >> t15
t10 >> t13 >> t15
t10 >> t14 >> t15
