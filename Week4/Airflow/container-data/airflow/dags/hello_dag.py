from datetime import datetime
from airflow import DAG, AirflowException
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from airflow.utils.trigger_rule import TriggerRule


def print_1():
    return 'Step 1'


def print_2():
    #raise AirflowException('Oops!') #Uncomment to make error
    return 'Step 2'


def print_3():
    return 'Step 3'


def print_hello():
    return 'Hello Wolrd'


dag = DAG('hello-world-dag',
          start_date=datetime(2020, 3, 10),
          description='Hello world example',
          schedule_interval='*/2 * * * *')

step1 = PythonOperator(task_id='step1', python_callable=print_1, dag=dag)
step2 = PythonOperator(task_id='step2', python_callable=print_2, dag=dag)
step3 = PythonOperator(task_id='step3', python_callable=print_3, dag=dag)
hello_operator = PythonOperator(task_id='hello_task',
                                python_callable=print_hello,
                                #trigger_rule=TriggerRule.ONE_SUCCESS, #Uncomment to skip error
                                dag=dag)

step1 >> [step2, step3]
step2 >> hello_operator
step3 >> hello_operator
