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