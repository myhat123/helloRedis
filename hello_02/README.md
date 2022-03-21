配置redis
========

hzg@gofast:~/redis-6.2.6$ ls
00-RELEASENOTES  COPYING   MANIFESTO   runtest-cluster    src
BUGS             deps      README.md   runtest-moduleapi  tests
CONDUCT          INSTALL   redis.conf  runtest-sentinel   TLS.md
CONTRIBUTING     Makefile  runtest     sentinel.conf      utils
hzg@gofast:~/redis-6.2.6$ 

配置文件 redis.conf

配置选项

port              6379
daemonize         yes          #后台运行yes 前台运行no
save              60 1
bind              127.0.0.1
tcp-keepalive     300
dbfilename        dump.rdb
dir               ./
rdbcompression    yes
user              hzg on #b63d0bd4aab9cfaae37b9d940218c3d1425383fd51cab522e1c5cb3191d47bd4 ~* +@all

$ ./src/redis-server redis.conf
$ ./src/redis-cli

hzg@gofast:~/redis-6.2.6$ ./src/redis-cli
127.0.0.1:6379> acl list
1) "user default on nopass ~* &* +@all"
127.0.0.1:6379> 

权限管理
=======

参考 https://www.cnblogs.com/zhoujinyi/p/13222464.html

$ echo -n "pydj1234" | shasum -a 256
b63d0bd4aab9cfaae37b9d940218c3d1425383fd51cab522e1c5cb3191d47bd4  -

在创建用户之前，先说明下ACL的规则，首先看下一个完整的用户权限的格式：

> ACL LIST  --显示用户信息
1) "user default on #b63d0bd4aab9cfaae37b9d940218c3d1425383fd51cab522e1c5cb3191d47bd4 ~* +@all"

格式说明：

参数说明

user       用户
default    表示默认用户名，或则自己定义的用户名
on	       表示是否启用该用户，默认为off（禁用）
#...	   表示用户密码，nopass表示不需要密码
~*	       表示可以访问的Key（正则匹配）
+@	       表示用户的权限，+/-表示授权还是销权； @为权限类。+@all 表示所有权限

hzg@gofast:~/redis-6.2.6$ ./src/redis-cli shutdown
(error) NOAUTH Authentication required.

hzg@gofast:~/redis-6.2.6$ ./src/redis-cli --user hzg --pass pydj1234
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
127.0.0.1:6379> shutdown
not connected> exit
hzg@gofast:~/redis-6.2.6$ 

hzg@gofast:~/redis-6.2.6$ ./src/redis-cli --user hzg --askpass
Please input password: ********
127.0.0.1:6379>

hzg@gofast:~/redis-6.2.6$ ./src/redis-cli --user hzg
127.0.0.1:6379> ping
PONG