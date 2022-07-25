from pyspark.sql import SparkSession


def main():
    spark = SparkSession \
        .builder \
        .appName("WordCountStream") \
        .getOrCreate()

    lines = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092,localhost:9093,localhost:9094") \
        .option("subscribe", "words") \
        .load()

    df = lines.selectExpr("CAST(value AS STRING)").alias("value")

    query = df \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()


if __name__ == "__main__":
    main()
