Logging In Remotely
-------------------

To give users access outside of localhost, first create a user with access to '%' (see below). You may also need to comment out the line in /etc/mysql/my.cnf to comment out the bind-address option.

Dumping a Table
---------------

Dumping a table to a MySQL-formatted SQL file:

```bash
mysqldump -u root -p my_database my_table > my_table.sql
```

Dumping a table to a CSV file:

```mysql
SELECT
    *
FROM
    mytable
INTO OUTFILE '/tmp/mytable.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```

Creating New Users
------------------

```mysql
DROP USER demo@'localhost';
DROP USER demo@'%';
CREATE USER 'demo'@'localhost' IDENTIFIED BY 'demo';
CREATE USER 'demo'@'%' IDENTIFIED BY 'demo';
GRANT ALL PRIVILEGES ON *.* TO 'demo'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'demo'@'%' WITH GRANT OPTION;
```

Viewing Users
-------------

```mysql
SELECT user, host, password FROM mysql.user;
```

Pretty-printing SQL
-------------------

The following is a nice web-based formatter with several options:

http://www.dpriver.com/pp/sqlformat.htm

STRAIGHT_JOIN
-------------

`STRAIGHT_JOIN` is an optimization for joins and is described here:

http://dev.mysql.com/doc/refman/5.0/en/join.html

Configuration
-------------

Configuration for MySQL can be stored in a file (including optional password) named $HOME/.my.cnf. The file can be as simple as:

    [client]
    password=53cr3t

Alternatively, you can set the `MYSQL_PWD` environment variable to your password, though this is obviously insecure.

Query Process Management
------------------------

To see all the queries in process:

```mysql
show [full] processlist
```

And to kill one:

```mysql
kill query <query ID>
```

Creating Tables from Queries
----------------------------

It's possible to create a table using the derived schema from an arbitrarily complex query. Here's a quick example:

```mysql
CREATE TABLE dst_tbl SELECT * FROM src_tbl;
```

There's a bit more information here:

http://answers.oreilly.com/topic/158-how-to-save-query-results-in-a-mysql-table/

Query Caching
-------------

You can disable the client-side query results cache in the `mysql` command line client thusly:

```mysql
SET SESSION query_cache_type = OFF;
```

Apparently you can add `SQL_NO_CACHE` to your query to cause the server to not cache the query results:

```mysql
SELECT SQL_NO_CACHE
    count(clicks)
FROM
    users
WHERE  
    name like 'Kirk%';
```

Determine Disk Usage
--------------------

In the `mysql` command line client:

```mysql
SELECT
    (data_length+index_length) / power(1024, 3) AS tablesize_gb
FROM
    information_schema.tables
WHERE
    table_schema = 'xxxx';
```

Viewing a Table Definition
--------------------------

Show the `CREATE TABLE` statement used to create table foo:

```mysql
SHOW CREATE TABLE foo;
```
