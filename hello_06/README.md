示例
====

事务

In redis-py, Pipeline is a transactional pipeline class by default. 

127.0.0.1:6379> MULTI
127.0.0.1:6379> HINCRBY 56854717 quantity -1
127.0.0.1:6379> HINCRBY 56854717 npurchased 1
127.0.0.1:6379> EXEC