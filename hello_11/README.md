进程池
=====

https://www.cnblogs.com/buyizhiyou/p/13438251.html

Pool可以提供指定数量的进程，供用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来它。

pool.apply_async(func, (msg, )) 非阻塞
pool.apply(func, (msg, )) 阻塞

返回结果，也可以放入队列 queue