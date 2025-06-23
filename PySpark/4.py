# handeling and replacing null values (na) how, thresh, subset
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Practice4').getOrCreate()

df = spark.read.csv(r'/home/mypc/Documents/Python/PySpark/4.csv', header=True, inferSchema=True)
df.show()

#drops all the null records in a table
df.na.drop(how="any").show()

#drops the records where null values exceeds specified
df.na.drop(thresh=2).show()

#drops the null record of a specified col only
df.na.drop(subset=['name']).show()