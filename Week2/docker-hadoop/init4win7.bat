@ECHO OFF
docker cp ./tmp/data namenode:/course/data
docker cp ./tmp/input namenode:/course/input
docker cp ./tmp/job namenode:/job
docker cp ./tmp/init namenode:/init
ECHO All data has been copied successfully.