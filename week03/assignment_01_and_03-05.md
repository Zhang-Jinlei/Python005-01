# 1、3、4、5 作业



## 1、

|                                                  |
| :----------------------------------------------- |
| CREATE DATABASE testdb;                          |
| SHOW VARIABLES LIKE '%character%';               |
| SET character_set_server='utf8mb4';              |
|                                                  |
| CREATE USER 'testuser' IDENTIFIED BY 'testpass'; |
| GRANT ALL ON testdb.* TO 'testuser'@'%';         |



## 3、



|                                                         |      |
| :------------------------------------------------------ | :--- |
| SELECT DISTINCT player_id, player_name, count(*) as num | # 5  |
| FROM player JOIN team ON player.team_id = team.team_id  | # 1  |
| WHERE height > 1.80                                     | # 2  |
| GROUP BY player.team_id                                 | # 3  |
| HAVING num > 2                                          | # 4  |
| ORDER BY num DESC                                       | # 6  |
| LIMIT 2                                                 | # 7  |



## 4、



| INNER JOIN |               |           |               |
| ---------- | :-----------: | :-------: | :-----------: |
| table1.id  |  table1.name  | table2.id |  table2.name  |
| 1          | table1_table2 |     1     | table1_table2 |



| LEFT JOIN |               |           |               |
| --------- | :-----------: | :-------: | :-----------: |
| table1.id |  table1.name  | table2.id |  table2.name  |
| 1         | table1_table2 |     1     | table1_table2 |
| 2         |    table1     |   NULL    |     NULL      |



| RIGHT JOIN |               |           |               |
| ---------- | :-----------: | :-------: | :-----------: |
| table1.id  |  table1.name  | table2.id |  table2.name  |
| 1          | table1_table2 |     1     | table1_table2 |
| NULL       |     NULL      |     3     |    table2     |



5、

|                                             |
| ------------------------------------------- |
| CREATE INDEX ix_table1_name ON table1(name) |
| CREATE INDEX ix_table2_name ON table2(name) |



这里直接引用即刻时间陈旸老师「SQL必知必会」 [23丨索引的概览：用还是不用索引，这是一个问题](https://time.geekbang.org/column/article/112023)

![jpg](https://github.com/Zhang-Jinlei/Python005-01/blob/main/week03/SQL必知必会_23丨索引的概览：用还是不用索引，这是一个问题.jpg?raw=true)
