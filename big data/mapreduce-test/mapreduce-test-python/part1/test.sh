#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /part1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/test.txt /part1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/part1/mapper-1.py -mapper ../../mapreduce-test-python/part1/mapper-1.py \
-file ../../mapreduce-test-python/part1/reducer-1.py -reducer ../../mapreduce-test-python/part1/reducer-1.py \
-input /part1/input/* -output /part1/output/


/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/part1/mapper-2.py -mapper ../../mapreduce-test-python/part1/mapper-2.py \
-file ../../mapreduce-test-python/part1/reducer-2.py -reducer ../../mapreduce-test-python/part1/reducer-2.py \
-input /part1/output/* -output /part1-2/output/





/usr/local/hadoop/bin/hdfs dfs -cat /part1-2/output/part-00000 | tail -10
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1-2/output/
../../stop.sh
