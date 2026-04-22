from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('temp').getOrCreate()
df=spark.read.option('header',True).option('inferSchema',True).csv(r'D:\Aman\aman.code\Databricks\movie.csv')

df.write.mode("overwrite").parquet("file:///D:/Aman/aman.code/Databricks/data")