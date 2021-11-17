# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 3:27 下午
# @Author  : Poppet 
# @Email   : suchenglong@linezonedata.com
# @File    : test_agg.y;.py
# @Software: PyCharm
from __future__ import print_function
import sys

from pyspark.sql import SparkSession
from pyspark import SparkConf
spark = SparkSession.builder.config(conf=SparkConf()).enableHiveSupport().getOrCreate()
inputPath = ""
mnm_df = spark.read.format('csv').option("header","true").option('inferSchema',"true").load(inputPath)

mnm_df.show(n=10, truncate=False)
count_mnm_df = mnm_df.select("State","Color","Count").groupBy("State","Color").sum("Count").orderBy("sum(Count)",ascending=False)
count_mnm_df.show()
