from pyspark.sql import SparkSession

# Start a Spark session
spark = SparkSession.builder.appName("Simple DataFrame").getOrCreate()

# Sample data (list of tuples)
data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 22)
]

# Define column names
columns = ["Name", "Age"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()
