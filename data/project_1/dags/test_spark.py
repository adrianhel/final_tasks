from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os


def test_pyspark():
    """Тестовая функция для проверки работы PySpark"""
    import findspark
    findspark.init()

    from pyspark.sql import SparkSession
    from pyspark.sql.types import StructType, StructField, StringType, IntegerType

    # Создаем Spark сессию
    spark = SparkSession.builder \
        .appName("AirflowPySparkTest") \
        .config("spark.sql.adaptive.enabled", "true") \
        .getOrCreate()

    try:
        # Создаем тестовые данные
        data = [
            ("Python", 1, "Data Engineering"),
            ("Spark", 2, "Data Processing"),
            ("Airflow", 3, "Orchestration"),
            ("Docker", 4, "Containerization")
        ]

        schema = StructType([
            StructField("Technology", StringType(), True),
            StructField("Rating", IntegerType(), True),
            StructField("Category", StringType(), True)
        ])

        # Создаем DataFrame
        df = spark.createDataFrame(data, schema)

        # Показываем данные
        print("=== Spark DataFrame ===")
        df.show()

        # Простая агрегация
        print("=== Aggregated Data ===")
        df.groupBy("Category").count().show()

        # Проверяем версии
        print(f"PySpark version: {spark.version}")
        print("PySpark test completed successfully!")

    except Exception as e:
        print(f"Error in Spark job: {e}")
        raise
    finally:
        # Всегда останавливаем Spark сессию
        spark.stop()


def test_java_home():
    """Проверка переменных окружения Java"""
    java_home = os.getenv('JAVA_HOME')
    spark_home = os.getenv('SPARK_HOME')

    print(f"JAVA_HOME: {java_home}")
    print(f"SPARK_HOME: {spark_home}")

    # Проверяем что Java доступна
    import subprocess
    try:
        result = subprocess.run(['java', '-version'], capture_output=True, text=True)
        print("Java version check:")
        print(result.stderr)
    except Exception as e:
        print(f"Java check failed: {e}")


with DAG(
        'test_pyspark_integration',
        start_date=datetime(2024, 1, 1),
        schedule_interval=None,
        catchup=False,
        tags=['test', 'pyspark'],
        default_args={
            'retries': 1,
        }
) as dag:
    check_environment = PythonOperator(
        task_id='check_java_environment',
        python_callable=test_java_home
    )

    test_spark = PythonOperator(
        task_id='test_pyspark_functionality',
        python_callable=test_pyspark
    )

    check_environment >> test_spark