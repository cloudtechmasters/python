    mysql> create database testdb;
    Query OK, 1 row affected (0.00 sec)
    
    mysql> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | mysql              |
    | performance_schema |
    | testdb             |
    +--------------------+
    4 rows in set (0.00 sec)
    
    mysql> use testdb;
    Database changed
    mysql> create table employee(emp_id int(10),emp_name varchar(40),emp_sal int(10));
    Query OK, 0 rows affected (0.04 sec)
    
    mysql> show tables;
    +------------------+
    | Tables_in_testdb |
    +------------------+
    | employee         |
    +------------------+
    1 row in set (0.00 sec)
    
    mysql> select * from employee;
    Empty set (0.00 sec)
    
    mysql> select * from employee;
    +--------+----------+---------+
    | emp_id | emp_name | emp_sal |
    +--------+----------+---------+
    |    100 | Tushar   |    1000 |
    +--------+----------+---------+
    1 row in set (0.00 sec)
    
    mysql> select * from employee;
    +--------+----------+---------+
    | emp_id | emp_name | emp_sal |
    +--------+----------+---------+
    |    100 | Tushar   |    1000 |
    |    101 | hrushi   |    2000 |
    |    200 | vihan    |    1200 |
    |    300 | ramesh   |    1500 |
    +--------+----------+---------+
    4 rows in set (0.00 sec)
    
    mysql> select * from employee;
    +--------+----------+---------+
    | emp_id | emp_name | emp_sal |
    +--------+----------+---------+
    |    100 | Tushar   |    1000 |
    |    101 | hrushi   |    2000 |
    |    200 | vihan    |    1200 |
    |    300 | ramesh   |    1500 |
    |    101 | hrushi   |    2000 |
    |    200 | vihan    |    1200 |
    |    300 | ramesh   |    1500 |
    +--------+----------+---------+
    7 rows in set (0.00 sec)
