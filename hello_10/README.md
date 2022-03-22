pika
====

落盘的redis版本，由360出品

https://github.com/OpenAtomFoundation/pika

文档: https://github.com/OpenAtomFoundation/pika/wiki

https://github.com/OpenAtomFoundation/pika/releases/download/v3.3.6/pika-linux-x86_64-v3.3.6.tar.bz2

解压之后

hzg@gofast:~/pika-3.3.6$ ./bin/pika -c ./conf/pika.conf
path : ./conf/pika.conf
-----------Pika server----------
pika_version: 3.3.6
pika_git_sha:9e74c8cd0040a0a63c35e9d426c7d3b6464b378e
pika_build_compile_date: Dec  4 2020
-----------Pika config list----------
 1 port 9221
 2 thread-num 1
 3 thread-pool-size 12
 4 sync-thread-num 6
 5 log-path ./log/
 6 db-path ./db/
 7 write-buffer-size 268435456
 8 arena-block-size 
 9 timeout 60
10 requirepass 
11 masterauth 
12 userpass 
13 userblacklist 
14 instance-mode classic
15 databases 1
16 default-slot-num 1024
17 replication-num 0
18 consensus-level 0
19 dump-prefix 
20 dump-path ./dump/
21 dump-expire 0
22 pidfile ./pika.pid
23 maxclients 20000
24 target-file-size-base 20971520
25 expire-logs-days 7
26 expire-logs-nums 10
27 root-connection-num 2
28 slowlog-write-errorlog no
29 slowlog-log-slower-than 10000
30 slowlog-max-len 128
31 db-sync-path ./dbsync/
32 db-sync-speed -1
33 slave-priority 100
34 sync-window-size 9000
35 max-conn-rbuf-size 268435456
36 write-binlog yes
37 binlog-file-size 104857600
38 max-cache-statistic-keys 0
39 small-compaction-threshold 5000
40 max-write-buffer-size 10737418240
41 max-write-buffer-number 2
42 max-client-response-size 1073741824
43 compression snappy
44 max-background-flushes 1
45 max-background-compactions 2
46 max-cache-files 5000
47 max-bytes-for-level-multiplier 10
-----------Pika config end----------

直接用redis-cli连接pika

hzg@gofast:~/redis-6.2.6$ ./src/redis-cli -p 9221
127.0.0.1:9221> acl list
(error) ERR unknown or unsupported command 'acl"
127.0.0.1:9221> ping
PONG
127.0.0.1:9221> set hi china
OK
127.0.0.1:9221> get hi
"china"
127.0.0.1:9221> 
