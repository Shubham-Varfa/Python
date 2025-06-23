# filter operation & | ~
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Practice2').getOrCreate()

df = spark.read.csv(r'/home/mypc/Documents/Python/PySpark/2.csv', header=True, inferSchema=True)
df.show()

df.filter(df['gender']=='F').show()

df.filter((df['salary']>=20000) & (df['gender']=='F') & (df['exp']>=10)).show()