批量删除key
==========

参考资料 

https://newbedev.com/redis-python-how-to-delete-all-keys-according-to-a-specific-pattern-in-python-without-python-iterating

for key in r.scan_iter("prefix:*"):
    r.delete(key)

第一版本:

from redis import StrictRedis
cache = StrictRedis()

def clear_ns(ns):
    """
    Clears a namespace
    :param ns: str, namespace i.e your:prefix
    :return: int, cleared keys
    """
    count = 0
    ns_keys = ns + '*'
    for key in cache.scan_iter(ns_keys):
        cache.delete(key)
        count += 1
    return count

第二版本:

from redis import StrictRedis
cache = StrictRedis()

def clear_cache_ns(ns):
    """
    Clears a namespace in redis cache.
    This may be very time consuming.
    :param ns: str, namespace i.e your:prefix*
    :return: int, num cleared keys
    """
    count = 0
    pipe = cache.pipeline()
    for key in cache.scan_iter(ns):
        pipe.delete(key)
        count += 1
    pipe.execute()
    return count

第三版本:

from redis import StrictRedis
cache = StrictRedis()
CHUNK_SIZE = 5000

def clear_ns(ns):
    """
    Clears a namespace
    :param ns: str, namespace i.e your:prefix
    :return: int, cleared keys
    """
    cursor = '0'
    ns_keys = ns + '*'
    while cursor != 0:
        cursor, keys = cache.scan(cursor=cursor, match=ns_keys, count=CHUNK_SIZE)
        if keys:
            cache.delete(*keys)

    return True