from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Create Spark session with Kafka integration
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .config("spark.sql.streaming.forceDeleteTempCheckpointLocation", "true") \
    .getOrCreate()

# Define schema for incoming data
schema = StructType([
    StructField("student_id", IntegerType(), True),
    StructField("subject", StringType(), True),
    StructField("marks", IntegerType(), True),
    StructField("grade", StringType(), True)
])

# Read from Kafka topic
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9093") \
    .option("subscribe", "test-topic") \
    .option("startingOffsets", "earliest") \
    .load()

# Parse Kafka message values as JSON
df_parsed = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Write the processed data to the console
query = df_parsed.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
