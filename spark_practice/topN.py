# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 3:04 下午
# @Author  : Poppet 
# @Email   : suchenglong@linezonedata.com
# @File    : topN.py.py
# @Software: PyCharm

from pyspark.sql import SparkSession
from pyspark import SparkConf

spark = SparkSession.builder.config(conf=SparkConf()).enableHiveSupport().getOrCreate()

nums = [1, 2, 3, 4, 5, 6, 8, 7]

print(spark.sparkContext.parallelize(nums).takeOrdered(3, key=lambda x: -x))

kv = [(10,"z1"), (1,"z2"), (2,"z3"), (9,"z4"), (3,"z5"), (4,"z6"), (5,"z7"), (6,"z8"), (7,"z9")]

print(spark.sparkContext.parallelize(kv).takeOrdered(3, key=lambda x: -x[0]))

