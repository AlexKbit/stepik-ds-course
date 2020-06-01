import io
import sys

from pyspark.ml import Pipeline
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.sql import SparkSession

# Используйте как путь куда сохранить модель
MODEL_PATH = 'spark_ml_model'


def process(spark, train_data):
    #train_data - путь к файлу с данными для обучения модели
    #Ваш код


def main(argv):
    train_data = argv[0]
    print("Input path to train data: " + train_data)
    spark = _spark_session()
    process(spark, train_data)


def _spark_session():
    return SparkSession.builder.appName('PySparkMLFitJob').getOrCreate()


if __name__ == "__main__":
    arg = sys.argv[1:]
    if len(arg) != 1:
        sys.exit("Train data are require.")
    else:
        main(arg)
