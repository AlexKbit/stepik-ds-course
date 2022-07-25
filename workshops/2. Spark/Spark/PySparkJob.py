import io
import sys
from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.appName('PySparkJob').getOrCreate()

if __name__ == "__main__":
    main()
