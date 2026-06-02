from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from kubernetes.client import models as k8s

default_args = {
    'owner': 'precedent_ia',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'pipeline_pangea_vetorial',
    default_args=default_args,
    description='Pipeline de extração do PANGEA para o Banco Vetorial',
    schedule_interval='@weekly', # Rodando a cada 7 dias (Critério de Aceite)
    catchup=False,
    max_active_runs=1
) as dag:

    # 1) Task de Scraping
    scraping_task = KubernetesPodOperator(
        namespace='precedentia-jobs', # Namespace onde os jobs vão rodar no K8s
        image='seu-registry.com/precedentia-scraper:latest', # A imagem Docker do seu submódulo
        cmds=["python", "main.py", "--run-scraper"], # Comando para iniciar o script
        name="pangea-scraper-pod",
        task_id="1_scraping",
        get_logs=True,
        is_delete_operator_pod=True, # Deleta o container após terminar com sucesso
    )

    # 2) Task de Embedding
    embedding_task = KubernetesPodOperator(
        namespace='precedentia-jobs',
        image='seu-registry.com/precedentia-embedding:latest',
        cmds=["python", "main.py", "--run-embedding"],
        name="pangea-embedding-pod",
        task_id="2_embedding",
        get_logs=True,
        is_delete_operator_pod=True,
    )

    # 3) Task de Summary
    summary_task = KubernetesPodOperator(
        namespace='precedentia-jobs',
        image='seu-registry.com/precedentia-summary:latest',
        cmds=["python", "main.py", "--run-summary"],
        name="pangea-summary-pod",
        task_id="3_summary",
        get_logs=True,
        is_delete_operator_pod=True,
    )

    # Definindo a ordem de execução (Critério de Aceite)
    scraping_task >> embedding_task >> summary_task