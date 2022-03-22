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

redis-py 封装了自己的解析器, PythonParser
hiredis 用c语言编写的库, 快速的解析器

pip install hiredis

```python
# redis/utils.py
try:
    import hiredis
    HIREDIS_AVAILABLE = True
except ImportError:
    HIREDIS_AVAILABLE = False


# redis/connection.py
if HIREDIS_AVAILABLE:
    DefaultParser = HiredisParser
else:
    DefaultParser = PythonParser
```

不需要直接使用hiredis，只需要安装即可。redis-py会自动判断是否使用。