import pyspark
from pyspark.sql import SparkSession
print('modules imported')

spark= SparkSession.builder.appName('spark_variables').getOrCreate()
print('app created')

sales_df = spark.read.format('jdbc'). \
    option('url', 'jdbc:oracle:thin:sh/sh@//localhost:1522/oracle'). \
    option('dbtable', 'sales'). \
    option('user', 'sh'). \
    option('password', 'sh'). \
    option('driver', 'oracle.jdbc.driver.OracleDriver').load()

sales_df.show(5)

#https://www.youtube.com/watch?v=RsALKtZvqFo
#https://www.pavanpkulkarni.com/blog/12-pyspark-in-pycharm/