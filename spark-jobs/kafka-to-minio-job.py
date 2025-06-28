from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import json

# Create Spark session with Avro support
spark = SparkSession.builder \
    .appName("KafkaToMinIO") \
    .config("spark.sql.streaming.checkpointLocation", "/tmp/checkpoint") \
    .getOrCreate()

# Read from Kafka with proper Avro deserialization
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "postgres-server.public.Ecommerce_Transactions,postgres-server.public.Chocolate_Sales_Data,postgres-server.public.Customer_Transactions_Dataset") \
    .option("startingOffsets", "latest") \
    .load()

# Convert Kafka value from binary to string
parsed_df = df.select(
    col("key").cast("string"),
    col("value").cast("string"),
    col("timestamp")
)

# STREAMING WRITE to MinIO
query = parsed_df.writeStream \
    .format("delta") \
    .option("checkpointLocation", "s3a://streamed-data/checkpoints/") \
    .option("path", "s3a://streamed-data/kafka-data/") \
    .outputMode("append") \
    .trigger(processingTime='30 seconds') \
    .start()

# Keep streaming alive
query.awaitTermination()