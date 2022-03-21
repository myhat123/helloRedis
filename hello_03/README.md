python和redis
=============

https://realpython.com/python-redis/

Redis stands for Remote Dictionary Service. 很有意思的说法

1. redis用法

127.0.0.1:6379> SET Bahamas Nassau
OK
127.0.0.1:6379> SET Croatia Zagreb
OK
127.0.0.1:6379> GET Croatia
"Zagreb"
127.0.0.1:6379> GET Japan
(nil)

相应的python dict

>>> capitals = {}
>>> capitals["Bahamas"] = "Nassau"
>>> capitals["Croatia"] = "Zagreb"
>>> capitals.get("Croatia")
'Zagreb'
>>> capitals.get("Japan")  # None

2. redis用法

127.0.0.1:6379> MSET Lebanon Beirut Norway Oslo France Paris
OK
127.0.0.1:6379> MGET Lebanon Norway Bahamas
1) "Beirut"
2) "Oslo"
3) "Nassau"

相应的python dict

>>> capitals.update({
...     "Lebanon": "Beirut",
...     "Norway": "Oslo",
...     "France": "Paris",
... })
>>> [capitals.get(k) for k in ("Lebanon", "Norway", "Bahamas")]
['Beirut', 'Oslo', 'Nassau']

3. redis用法

127.0.0.1:6379> EXISTS Norway
(integer) 1
127.0.0.1:6379> EXISTS Sweden
(integer) 0

相应的python

>>> "Norway" in capitals
True
>>> "Sweden" in capitals
False

Python Redis client library, redis-py
REdis Serialization Protocol (RESP) redis协议

pip install redis

redis-py的文档 https://redis-py.readthedocs.io/en/stable/

>>> import redis
>>> r = redis.Redis()
>>> r.ping()
True
>>> 

redis://[[username]:[password]]@localhost:6379/0

>>> r = redis.from_url('redis://hzg:pydj1234@localhost:6379')
>>> r.ping()
True

https://www.runoob.com/w3cnote/python-redis-intro.html

>>> r = redis.Redis(host='localhost', port=6379, decode_responses=True)

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

管道（pipeline）
redis默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。

管道（pipeline）是redis在提供单个请求中缓冲多条服务器命令的基类的子类。它通过减少服务器-客户端之间反复的TCP数据库包，从而大大提高了执行批量命令的功能。