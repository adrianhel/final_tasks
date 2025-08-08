from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum, to_date


spark = SparkSession.builder \
                    .appName("Log Analysis") \
                    .getOrCreate()

logs_df = spark.read.csv("web_server_logs.csv", header=True, inferSchema=True)


active_ips = logs_df.groupBy("ip").agg(count("*").alias("request_count")) \
                                  .orderBy(col("request_count").desc()) \
                                  .limit(10)

print("Top 10 active IP addresses:")
active_ips.show()


http_methods = logs_df.groupBy("method").agg(count("*").alias("request_count"))

print("Request count by HTTP method:")
http_methods.show()


not_found_count = logs_df.filter(col("response_code") == 404).count()

print(f"Number of 404 response codes: {not_found_count}")


response_size_by_date = logs_df.groupBy(to_date(col("timestamp")).alias("date")) \
                               .agg(sum("response_size").alias("total_response_size")) \
                               .orderBy("date")

print("Total response size by day:")
response_size_by_date.show()


spark.stop()
