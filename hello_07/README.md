Redis加快批量插入数据速度的方法: redis pipline 分块插入

https://www.jianshu.com/p/b049feb67524

利用redis pipline 管道技术
把需要插入的数据分块批量插入

举个例子需要添加3000万的数字用于后面分布式爬虫构造url，现在需要把3000万的数字插入redis数据库。

1. 普通的插入redis set集合方法

r = redis.Redis(host="127.0.0.1", port=6379)
for i in range(1, 3 * 10 ** 8):
    r.sadd('xxxxx', i)

2. 利用redis pipline 管道技术

r = redis.Redis(host="127.0.0.1", port=6379)
pipeline = r.pipeline()
for i in range(1, 3 * 10 ** 8):
    pipeline.sadd('xxxxx', i)
pipeline.execute()

这种操作相当于写了一堆的命令一次性执行完，一旦某个命令出问题那么这次插入数据就会失败。这种方式的好处。节省了本机与redis服务器链接的 IO 延时，一般来说节省了很多时间。

3. 把需要插入的数据分块批量插入

for i in range(30):
   ls = list(range(i*1000000,(i+1)*1000000))
   r.sadd('xxxxx', *ls)

如果需要插入的数据不是这里的数字分块方法就需要换了，这样的方式是一次插入多个数据，不会出现使用pipline如果某个命令出问题就全部插入失败的现象，速度非常快，比使用pipline 的方式快了几倍。