echo 'Copy require data to containers'
docker cp data/checkdata.txt namenode:/tmp/checkdata.txt
echo 'Upload to HDFS'
docker exec -it namenode hdfs dfs -mkdir /data
docker exec -it namenode hdfs dfs -put /tmp/checkdata.txt /data/checkdata.txt
echo 'End'
