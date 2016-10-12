# Initializing Spark in Python
# needed to be launched with bin/spark-submit from cmd/terminal:
# e.g.,  
# bin/spark-submit path_to_my_script/my_script.py
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("App Demo: Line Count")
sc = SparkContext(conf = conf)

lines = sc.textFile("README.md")
pythonLines = lines.filter(lambda line: "Python" in line)
pythonLines.count()