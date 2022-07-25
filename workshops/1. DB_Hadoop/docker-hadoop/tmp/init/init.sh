#!/usr/bin/env bash
hdfs dfs -mkdir /data
hdfs dfs -mkdir /input
hdfs dfs -put /course/data/* /data/
hdfs dfs -put /course/input/* /input/
echo "Initialization complete"