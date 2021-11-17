# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 10:50 上午
# @Author  : Poppet 
# @Email   : suchenglong@linezonedata.com
# @File    : sql_practice.py.py
# @Software: PyCharm
from pyspark.sql import SparkSession
from pyspark import SparkConf

spark = SparkSession.builder.config(conf=SparkConf()).enableHiveSupport().getOrCreate()
sql = "show databases"
spark.sql(sql).show()


