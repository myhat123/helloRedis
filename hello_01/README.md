redis安装
=========

https://download.redis.io/releases/redis-6.2.6.tar.gz

解压

hzg@gofast:~/redis-6.2.6$ ls
00-RELEASENOTES  COPYING   MANIFESTO   runtest-cluster    src
BUGS             deps      README.md   runtest-moduleapi  tests
CONDUCT          INSTALL   redis.conf  runtest-sentinel   TLS.md
CONTRIBUTING     Makefile  runtest     sentinel.conf      utils

编译

$ make
...

    CC monotonic.o
    CC mt19937-64.o
    LINK redis-server
    INSTALL redis-sentinel
    CC redis-cli.o
    CC cli_common.o
    LINK redis-cli
    CC redis-benchmark.o
    LINK redis-benchmark
    INSTALL redis-check-rdb
    INSTALL redis-check-aof

Hint: It's a good idea to run 'make test' ;)

make[1]: 离开目录“/home/hzg/redis-6.2.6/src”
hzg@gofast:~/redis-6.2.6$ 

src目录下有 redis-server redis-cli