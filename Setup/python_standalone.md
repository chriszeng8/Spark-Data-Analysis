## 1. Standalone Application (execute scripts outside spark shell)

Standalone python script can be executed outside the context of spark shell. However, it must be run with bin/spark-submit script included in spark. The spark-submit script includes the Spark's python depencies, and set up the environment for Spark's python API. In the command prompt,

```bin/spark-submit my_script.py```

## 2. Initializing a SparkContext (create spark configuration and spark context)

Inside my_script.py, we need to initializing a SparkContext (i.e., sc).
```
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("Demo App: Line Count")
sc = SparkContext(conf = conf)
```

Two parameters required: 
* A cluster URL: namely "local" in this case
* An application name: which appears on top right corner of UI when go to port 4040 UI page.

## 3. After Initialization
After initialization, we can use all methods as before.

```
lines = sc.textFile("README.md")
pythonLines = lines.filter(lambda line: "Python" in line)
pythonLines.count()
```