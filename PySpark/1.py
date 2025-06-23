# from module import class
from pyspark.sql import SparkSession

# create a SparkSession
spark = SparkSession.builder.appName('Practice1').getOrCreate()

# read the (csv) file
df = spark.read.csv(r'/home/mypc/Documents/Python/PySpark/1.csv', header=True,inferSchema=True)
df.show()

#print the schema and data types
df.printSchema()

# prints a list of specified rows
print(df.head(5))

# print the column names
print(df.columns)

# show only specified cols
df.select(['id','name']).show()

# show count,mean, standard dev, min, max
df.describe().show()

# add a new col based on existing one
df = df.withColumn('CGPA', df['percentage']/10)

# drop a col
df = df.drop('percentage')

# rename col
df = df.withColumnRenamed('sex', 'gender')

df.show()

# stop the SparkSession
spark.stop()

