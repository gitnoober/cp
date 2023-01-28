import logging

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(filename="doc_creation_task.log", format=LOG_FORMAT)
log = logging.getLogger("DocCreation")
log.setLevel(logging.DEBUG)


def run(*args, **kwargs):
    log.info("Starting Doc Creation Download cron...")


default_args = {
    "owner": "Priyanshu",
    "depends_on_past": False,
    "start_date": days_ago(1),
    "email_on_failure": True,
    "email": ["priyanshu.singh@pocketfm.com"],
}

dag = DAG(
    dag_id="doc_creation_task",
    default_args=default_args,
    schedule_interval="0 */6 * * *",
    catchup=False,
)

run = PythonOperator(
    task_id="run",
    python_callable=run,
    email_on_failure=True,
    email="priyanshu.singh@pocketfm.com",
    dag=dag,
    depends_on_past=False,
)

doc_creation_task = BashOperator(
    task_id="doc_creation_task",
    bash_command="""ssh -o StrictHostKeyChecking=no -i ~/crawling_machine_key_pair.pem  ec2-user@13.213.61.176 'sudo su -c "source /home/ec2-user/venv/bin/activate; cd /home/ec2-user/airflow/dags; python -m novels_cron.cms.task_scheduler.doc_creation_task"' """,
    dag=dag,
)

run >> doc_creation_task