# etl_run_dag.py (Airflow 3 compatible)
from datetime import timedelta
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import timezone
import os

PROJECT_DIR = "/opt/airflow/mini-etl"
ETL_PY = os.path.join(PROJECT_DIR, "etl.py")

with DAG(
    dag_id="run_etl_docker",
    schedule=None,
    start_date=timezone.utcnow() - timedelta(days=1),
    catchup=False,
    tags=["mini-etl"],
) as dag:

    run_etl = BashOperator(
        task_id="run_python_etl",
        bash_command=(
            """bash -lc '
python - <<PY
import importlib, sys
reqs = ["minio", "pandas", "sqlalchemy", "psycopg2"]
missing = [r for r in reqs if importlib.util.find_spec(r) is None]
if missing:
    print("Missing packages:", missing)
    sys.exit(1)
else:
    print("All required packages present")
    sys.exit(0)
PY
' || python -m pip install --no-cache-dir -r /opt/airflow/mini-etl/requirements.txt && python /opt/airflow/mini-etl/etl.py
"""
        ),
        env={"PYTHONUNBUFFERED": "1"},
    )
