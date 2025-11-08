from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os


def test_spark():
    import findspark
    findspark.init()

    from pyspark.sql import SparkSession

    spark = SparkSession.builder \
        .appName("AirflowSparkTest") \
        .config("spark.sql.adaptive.enabled", "true") \
        .getOrCreate()

    # Простой тест
    data = [("Python", 1), ("Spark", 2), ("Airflow", 3)]
    df = spark.createDataFrame(data, ["Technology", "Rating"])
    df.show()

    print("Spark test completed successfully!")
    spark.stop()


with DAG(
        'test_spark_integration',
        start_date=datetime(2024, 1, 1),
        schedule_interval=None,
        catchup=False,
        tags=['test', 'spark']
) as dag:
    test_task = PythonOperator(
        task_id='test_spark_connection',
        python_callable=test_spark
    )