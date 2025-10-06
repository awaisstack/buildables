from minio import Minio
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import date
import os

# MinIO config — use env vars when running in container
MINIO_ENDPOINT = os.environ.get("MINIO_ENDPOINT", "minio:9000")  # 'minio:9000' for container-to-container
MINIO_ACCESS = os.environ.get("MINIO_ACCESS", "minioadmin")
MINIO_SECRET = os.environ.get("MINIO_SECRET", "minioadmin123")
BUCKET_IN = os.environ.get("BUCKET_IN", "landing")
OBJECT_IN = os.environ.get("OBJECT_IN", "employees_large.csv")
BUCKET_OUT = os.environ.get("BUCKET_OUT", "processed")
OBJECT_OUT = os.environ.get("OBJECT_OUT", "employees_summary.csv")

# Postgres config — default to Docker service name 'postgres'
PG_USER = os.environ.get("PG_USER", "etl_user")
PG_PASS = os.environ.get("PG_PASS", "etl_pass")
PG_HOST = os.environ.get("PG_HOST", "postgres")   # inside container use service name
PG_PORT = os.environ.get("PG_PORT", "5432")
PG_DB = os.environ.get("PG_DB", "etl_demo")

def ensure_output_bucket(client):
    if not client.bucket_exists(BUCKET_OUT):
        client.make_bucket(BUCKET_OUT)
        print("Created output bucket:", BUCKET_OUT)

def download_from_minio(client, local_path="/tmp/employees_large.csv"):
    print("Downloading from MinIO...")
    client.fget_object(BUCKET_IN, OBJECT_IN, local_path)
    print("Downloaded to", local_path)
    return local_path

def transform(path):
    print("Transforming data...")
    df = pd.read_csv(path)
    # Normalizing column names
    df.columns = [c.strip().lower() for c in df.columns]
    # Trimming strings
    for col in ['name','email','department','location','remote']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
    # Enforcing types
    df['emp_id'] = pd.to_numeric(df['emp_id'], errors='coerce').astype('Int64')
    df['salary'] = pd.to_numeric(df['salary'], errors='coerce').fillna(0).astype(int)
    df['hire_date'] = pd.to_datetime(df['hire_date'], errors='coerce')
    # Standardizing department
    if 'department' in df.columns:
        df['department'] = df['department'].str.title()
    # Dropping duplicates and rows missing emp_id or name
    df = df.drop_duplicates().dropna(subset=['emp_id','name'])
    # Creatingtenure (years)
    df['tenure_years'] = ((pd.Timestamp(date.today()) - df['hire_date']).dt.days / 365).round(2)
    # Performance bucketing and QC
    if 'performance_score' in df.columns:
        df['performance_score'] = pd.to_numeric(df['performance_score'], errors='coerce').clip(1.0,5.0)
        df['perf_bucket'] = pd.cut(df['performance_score'], bins=[0,2.5,3.5,5.1], labels=['Low','Medium','High'])
    # Salary bucket
    df['salary_bucket'] = pd.cut(df['salary'], bins=[0,30000,50000,70000,1000000], labels=['Entry','Junior','Mid','Senior'])
    # Quick QC: flag unrealistic salaries
    df.loc[(df['salary'] < 0) | (df['salary'] > 5_000_000), 'salary'] = None
    print("Transformed rows:", len(df))
    return df

def load_to_postgres(df, table_name="employees"):
    print("Loading into Postgres...")
    url = f"postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}"
    engine = create_engine(url)
    with engine.begin() as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        r = conn.execute(text(f"SELECT count(*) FROM {table_name}"))
        print("Rows in table:", r.scalar())

def create_summary_and_upload(df, client):
    # Create simple agg by department
    summary = df.groupby('department', dropna=False).agg(
        employees=('emp_id','count'),
        avg_salary=('salary','mean'),
        avg_perf=('performance_score','mean')
    ).reset_index()
    summary['avg_salary'] = summary['avg_salary'].round(2)
    # Save locally then upload to MinIO
    local = os.path.join(os.getcwd(), "employees_summary.csv")
    summary.to_csv(local, index=False)
    client.fput_object(BUCKET_OUT, OBJECT_OUT, local)
    print("Uploaded summary to MinIO:", f"{BUCKET_OUT}/{OBJECT_OUT}")
    return summary

def main():
    # MinIO client
    client = Minio(MINIO_ENDPOINT, access_key=MINIO_ACCESS, secret_key=MINIO_SECRET, secure=False)
    ensure_output_bucket(client)
    local_path = download_from_minio(client, local_path="employees_large.csv")
    df = transform(local_path)
    load_to_postgres(df)
    summary = create_summary_and_upload(df, client)
    print("Summary sample:")
    print(summary.head())

if __name__ == "__main__":
    main()
