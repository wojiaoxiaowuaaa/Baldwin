"""
https://github.com/wojiaoxiaowuaaa/go-stress-testing

https://www.cnblogs.com/Detector/p/17533341.html

高并发是一个相对概念，其具体的QPS（Queries Per Second）定义相对而言。一般情况下，高并发指的是系统单服务器同时处理的请求数量非常大，而且处理时间相对较短，即每秒的请求数量非常高。因此，对于不同的应用场景，划分高并发的QPS也会有所不同。
在一些小型的网站系统中，一秒钟处理1000个请求已经可以算作是高并发了。而对于大型应用，QPS可能需要达到几万甚至几十万个以上，例如高并发的电商网站、金融系统等。因此，高并发的定义取决于实际应用场景，需要根据系统的实际情况来评估其QPS。

locust中self.client调用get和post方法，跟requests请求一样哦。

-r  Hatch rate (users spawned/second)：每秒启动的虚拟用户数

-f 启动图形界面  locust -f demo.py

Requests  请求的总量

Average size 单个请求的大小，单位字节

Current RPS 代表吞吐量(Requests Per Second的缩写)，指的是某个并发用户数下单位时间内处理的请求数。等效于QPS，其实可以看作同一个统计方式，只是叫法不同而已。
"""