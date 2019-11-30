import io
import sys
from pyspark.sql import SparkSession


def process(spark, input_path, target_path):
    print("You code here.") #TODO YOUR CODE


def main(argv):
    input_path = argv[0]
    print("Input path: " + input_path)
    target_path = argv[1]
    print("Target path: " + target_path)
    spark = _spark_session()
    process(spark, input_path, target_path)


def _spark_session():
    return SparkSession.builder.appName('PySparkJob').getOrCreate()


if __name__ == "__main__":
    arg = sys.argv[1:]
    if len(arg) != 2:
        sys.exit("Input and Target path are require.")
    else:
        main(arg)
