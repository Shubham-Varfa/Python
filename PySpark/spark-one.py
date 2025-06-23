from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.getOrCreate()

# Create sample data
row = [("Bob", 23), ("Casey", 21), ("Reo", 25), ("Joe", 19), ("Dom", 30), ("Shakira", 22), ("Ken", 20)]
columns = ["Name", "Age"]

# Create DataFrame
df = spark.createDataFrame(row, columns)

# Show DataFrame
df.show()

# Filter Data
df.filter(df.Age > 22).show()

# Stop Spark session
spark.stop()
