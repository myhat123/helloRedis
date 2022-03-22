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
user              myhat123 on #03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4 ~* +@all
user              default off nopass ~* &* +@all

$ ./src/redis-server redis.conf
$ ./src/redis-cli

hzg@gofast:~/redis-6.2.6$ ./src/redis-cli
127.0.0.1:6379> acl list
1) "user default on nopass ~* &* +@all"
127.0.0.1:6379> 

权限管理
=======

参考 https://www.cnblogs.com/zhoujinyi/p/13222464.html

$ echo -n "1234" | shasum -a 256
03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4  -

在创建用户之前，先说明下ACL的规则，首先看下一个完整的用户权限的格式：

hzg@gofast:~/redis-6.2.6$ ./src/redis-cli --user myhat123 --askpass
Please input password: ****
127.0.0.1:6379> acl list
1) "user default off nopass sanitize-payload ~* &* +@all"
2) "user myhat123 on #03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4 ~* &* +@all"

格式说明：

参数说明

user       用户
default    表示默认用户名，或则自己定义的用户名
on	       表示是否启用该用户，默认为off（禁用）
#...	   表示用户密码，nopass表示不需要密码
~*	       表示可以访问的Key（正则匹配）
+@	       表示用户的权限，+/-表示授权还是销权； @为权限类。+@all 表示所有权限

关闭default默认用户后:

hzg@gofast:~/redis-6.2.6$ ./src/redis-cli
127.0.0.1:6379> acl list
(error) NOAUTH Authentication required.
127.0.0.1:6379> 
hzg@gofast:~/redis-6.2.6$ ./src/redis-cli --user myhat123
127.0.0.1:6379> acl list
(error) NOAUTH Authentication required.
127.0.0.1:6379> ping
(error) NOAUTH Authentication required.
127.0.0.1:6379> ping [message]
hzg@gofast:~/redis-6.2.6$ ./src/redis-cli --user myhat123 --askpass
Please input password: ****
127.0.0.1:6379> ping
PONG
127.0.0.1:6379> acl list
1) "user default off nopass sanitize-payload ~* &* +@all"
2) "user myhat123 on #03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4 ~* &* +@all"
127.0.0.1:6379> shutdown
not connected>

127.0.0.1:6379> ACL GETUSER myhat123
 1) "flags"
 2) 1) "on"
    2) "allkeys"
    3) "allchannels"
    4) "allcommands"
 3) "passwords"
 4) 1) "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
 5) "commands"
 6) "+@all"
 7) "keys"
 8) 1) "*"
 9) "channels"
10) 1) "*"
127.0.0.1:6379> auth myhat123 1234
OK

权限文件
=======

aclfile /home/hzg/etc/users.acl

users.acl内容

user              myhat123 on #03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4 ~* +@all
user              default off nopass ~* &* +@all