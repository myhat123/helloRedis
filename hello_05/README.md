redis-py使用
===========

>>> import redis
>>> r = redis.Redis()
>>> r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
True
>>> r.get("Bahamas")
b'Nassau'
>>> r.get("Bahamas").decode("utf-8")


# From redis/client.py
class Redis(object):
    def __init__(self, host='localhost', port=6379,
                 db=0, password=None, socket_timeout=None,
                 # ...

The db parameter is the database number. You can manage multiple databases in Redis at once, and each is identified by an integer. The max number of databases is 16 by default.

默认最大16个数据库，整型数字

命令行指定数据库: redis-cli -n 5

redis-py requires that you pass it keys that are bytes, str, int, or float. 

>>> import datetime
>>> today = datetime.date.today()
>>> visitors = {"dan", "jon", "alex"}
>>> r.sadd(today, *visitors)
Traceback (most recent call last):
# ...
redis.exceptions.DataError: Invalid input of type: 'date'.
Convert to a byte, string or number first.

>>> stoday = today.isoformat()  # Python 3.7+, or use str(today)
>>> stoday
'2019-03-10'
>>> r.sadd(stoday, *visitors)  # sadd: set-add
3
>>> r.smembers(stoday)
{b'dan', b'alex', b'jon'}
>>> r.scard(today.isoformat())
3