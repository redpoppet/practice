# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 1:29 下午
# @Author  : Poppet 
# @Email   : suchenglong@linezonedata.com
# @File    : word_count.py.py
# @Software: PyCharm

from pyspark.sql import SparkSession
from pyspark import SparkConf

spark = SparkSession.builder.master('local[*]').appName('wordCount').config(
    conf=SparkConf()).enableHiveSupport().getOrCreate()
inputPath = '/Users/poppet/workspace/practice/算法情况介绍.md'
lines = spark.read.text(inputPath).rdd.map(lambda r: r[0])
counts = lines.flatMap(lambda x: x.split(' ')).map(lambda  x:(x,1)).reduceByKey((lambda x,y:x+y ))
# counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
output = counts.collect()
print(output)
