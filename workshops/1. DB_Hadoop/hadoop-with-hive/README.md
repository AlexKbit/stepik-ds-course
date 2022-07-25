
## Testing
Load data into Hive:
```
  docker-compose exec hive-server bash

  hdfs dfs -mkdir /data

  hdfs dfs -put /data/users_20210501.csv /data
  hdfs dfs -put /data/users_20210502.csv /data

  hive

  CREATE EXTERNAL TABLE IF NOT EXISTS users(
          id INT,
          login STRING,
          email STRING,
          active BOOLEAN,
          organization_id INT)
      ROW FORMAT DELIMITED
      FIELDS TERMINATED BY ','
      STORED AS TEXTFILE
      location 'hdfs:///data';

```
