#### 备份数据库数据的命令：mysqldump

- 收集主机原有数据

  ```python
  mysqldump -uroot -p123456 -h172.18.222.232 --port=3307 demo > data.sql
  ```

- 从机复制主机原有数据

  ```python
  mysql -uroot -p123456 -h172.18.222.232 --port=3308 demo < data.sql
  ```

把 命令写进shell脚本，创建定时任务执行脚本





#### 慢查询日志

慢查询日志默认是关闭的 。可以通过两个参数来控制慢查询日志 :

```sql
# 该参数用来控制慢查询日志是否开启， 可取值: 1 和 0 ， 1 代表开启， 0 代表关闭 
slow_query_log=1

# 该参数用来指定慢查询日志的文件名
slow_query_log_file=/var/log/mysql/slow_query.log

# 该选项用来配置查询的时间限制， 超过这个时间将认为值慢查询， 将需要进行日志记录， 默认10s 
long_query_time=10
```





#### 开启MySQL日志

修改配置文件

```python
general_log_file        = /var/log/mysql/mysql.log
general_log             = 1
```

作用：记录sql语句

tail -f mysql.log

