更多数据类型
==========

A hash is a mapping of string:string, called field-value pairs, that sits under one top-level key:

127.0.0.1:6379> HSET realpython url "https://realpython.com/"
(integer) 1
127.0.0.1:6379> HSET realpython github realpython
(integer) 1
127.0.0.1:6379> HSET realpython fullname "Real Python"
(integer) 1

data = {
    "realpython": {
        "url": "https://realpython.com/",
        "github": "realpython",
        "fullname": "Real Python",
    }
}

127.0.0.1:6379> HMSET pypa url "https://www.pypa.io/" github pypa fullname "Python Packaging Authority"
OK
127.0.0.1:6379> HGETALL pypa
1) "url"
2) "https://www.pypa.io/"
3) "github"
4) "pypa"
5) "fullname"
6) "Python Packaging Authority"

Two additional value types are lists and sets, which can take the place of a hash or string as a Redis value. They are largely what they sound like, so I won’t take up your time with additional examples. Hashes, lists, and sets each have some commands that are particular to that given data type, which are in some cases denoted by their initial letter:

Hashes: Commands to operate on hashes begin with an H, such as HSET, HGET, or HMSET.

Sets: Commands to operate on sets begin with an S, such as SCARD, which gets the number of elements at the set value corresponding to a given key.

Lists: Commands to operate on lists begin with an L or R. Examples include LPOP and RPUSH. The L or R refers to which side of the list is operated on. A few list commands are also prefaced with a B, which means blocking. A blocking operation doesn’t let other operations interrupt it while it’s executing. For instance, BLPOP executes a blocking left-pop on a list structure.

Type	Commands
Sets	SADD, SCARD, SDIFF, SDIFFSTORE, SINTER, SINTERSTORE, SISMEMBER, SMEMBERS, SMOVE, SPOP,        
        SRANDMEMBER, SREM, SSCAN, SUNION, SUNIONSTORE
Hashes	HDEL, HEXISTS, HGET, HGETALL, HINCRBY, HINCRBYFLOAT, HKEYS, HLEN, HMGET, HMSET, HSCAN, HSET, 
        HSETNX, HSTRLEN, HVALS
Lists	BLPOP, BRPOP, BRPOPLPUSH, LINDEX, LINSERT, LLEN, LPOP, LPUSH, LPUSHX, LRANGE, LREM, LSET, LTRIM, 
        RPOP, RPOPLPUSH, RPUSH, RPUSHX
Strings	APPEND, BITCOUNT, BITFIELD, BITOP, BITPOS, DECR, DECRBY, GET, GETBIT, GETRANGE, GETSET, INCR, 
        INCRBY, INCRBYFLOAT, MGET, MSET, MSETNX, PSETEX, SET, SETBIT, SETEX, SETNX, SETRANGE, STRLEN

127.0.0.1:6379> FLUSHDB
OK
127.0.0.1:6379> QUIT