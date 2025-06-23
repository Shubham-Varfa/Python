# import 'SparkSession' class from 'pyspark.sql' module
from pyspark.sql import SparkSession # entry point for the spark

spark = SparkSession.builder.getOrCreate() # create a SparkSession named spark
# SparkSession sets the configuration to start the sperk
# .getOrCreate() will return an existing session if one is already active, or create a new one.

file_path = "/home/mypc/Downloads/color_srgb.csv" # storing the csv path in file_path variable

color = spark.read.csv(file_path, header = True) # reads the CSV file using the Spark session.
color.show() # displays 20 rows of the color DataFrame

#Check the Type of Data
print(type(color))

# Check the Scheme
color.printSchema()

# View Only Column Names
print(color.columns)
