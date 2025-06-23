# groupBy and aggrigate
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Practice3').getOrCreate()

df = spark.read.csv(r'/home/mypc/Documents/Python/PySpark/3.csv', header=True, inferSchema=True)

df.show()


df.groupBy('dep').sum('salary').show()