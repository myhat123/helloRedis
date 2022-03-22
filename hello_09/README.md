hiredis
=======

REdis Serialization Protocol, or RESP

redis协议 https://zhuanlan.zhihu.com/p/25577607

redis-py实现了redis协议

RESP 主要可以序列化以下几种类型：整数，单行回复(简单字符串)，数组，错误信息，多行字符串。
协议的每部分都是以 “\r\n” (CRLF) 结尾的

在 RESP 中, 一些数据的类型通过它的第一个字节进行判断：

单行回复：回复的第一个字节是 “+”
错误信息：回复的第一个字节是 “-“
整形数字：回复的第一个字节是 “:”
多行字符串：回复的第一个字节是 “$“
数组：回复的第一个字节是 “*”