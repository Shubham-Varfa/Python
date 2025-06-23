from pyspark.sql import SparkSession

# Create Spark session with JDBC driver
spark = SparkSession.builder \
    .appName("Simple SQLite ETL") \
    .config("spark.jars", "/home/mypc/Downloads/sqlite-jdbc-3.28.0.jar") \
    .getOrCreate()

# JDBC URL (use absolute path to your SQLite DB)
jdbc_url = "jdbc:sqlite:/home/mypc/Documents/Python/PySpark/test.db"

# Step 1: Extract data from users table
df = spark.read.format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", "users") \
    .option("driver", "org.sqlite.JDBC") \
    .load()
df.show()

# Step 2: Transform - filter users older than 18
df_filtered = df.filter(df.age > 18)

# Step 3: Load - write to a new table users_filtered
df_filtered.write.format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", "users_filtered") \
    .option("driver", "org.sqlite.JDBC") \
    .mode("overwrite") \
    .save()

df_filtered.show()


# Done
spark.stop()
