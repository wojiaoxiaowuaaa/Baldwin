# Locust 压力测试框架简介

Locust 是一个用于进行负载测试和性能测试的开源工具。其中文意思为蝗虫，寓意成片的蝗虫般扑向目标服务，对其进行压力测试。

## 主要优势

Locust 的主要优势在于完全基于事件驱动，使用 gevent 提供的非阻塞 IO 和协程来实现网络层的并发请求。即使在单台压力机上，也能产生数千并发请求，同时支持分布式部署。这使得 Locust 在模拟大量用户同时访问目标服务时表现出色。

## 快速上手示例

以下是一个简单的 Locust 压测脚本示例：

```python
from yace import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://127.0.0.1:9876"

    @task
    def index(self):
        self.client.get("/index")
```

上述脚本定义了一个继承自 `HttpUser` 的任务类 `QuickstartUser`。在任务类中，使用 `@task` 装饰器定义了一个简单的请求 `/index`。通过调整 `wait_time` 来模拟用户在任务之间的等待时间。

## 分布式压测脚本示例

如果你需要进行分布式压测，可以使用以下示例：

```python
from yace import HttpUser, TaskSet, between, task


class WebsiteTask(TaskSet):

    @task
    def index(self):
        self.client.get('/index')


class WebsiteUser(HttpUser):
    tasks = [WebsiteTask]
    host = 'http://127.0.0.1:9876'
```

## 终端执行压测

在终端中，可以使用以下命令执行压测脚本：

```bash
yace -f your_locust_file.py --headless -u 1000 -r 1000 -t 3600 --html=report.html
```

这个命令使用 Locust 进行压测，配置了一些参数，包括虚拟用户数量、每秒产生的虚拟用户数、压测时间和生成 HTML 报告。这将模拟 1000 个用户，每秒产生 1000 个用户，并持续压测 3600 秒，最终生成一个 HTML 报告。

Locust是一款非常流行的Python负载测试工具，可以模拟大量用户访问和请求，支持多种协议和格式。以下是使用Locust针对项目后端做性能测试的步骤和关注的指标:


### 关注的指标

1. 响应时间（Response Time）：响应时间指的是系统处理请求所需的时间，包括客户端发送请求、服务器处理请求和返回响应等所有时间。响应时间越短，表示系统响应速度越快。

2. 错误率（Error Rate）：错误率指的是请求失败的比例，包括HTTP错误、网络错误、服务器错误等。错误率越低，表示系统越稳定。

3. 吞吐量（Throughput）：吞吐量指的是系统在一定时间内处理的事务或请求的数量。通常以每秒钟处理的请求数（QPS）或每分钟处理的事务数（TPS）来衡量。吞吐量越高，表示系统处理能力越强。

### 测试脚本

```python
from yace import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def index_page(self):
        self.client.get("/")

    @task(3)
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")

    def on_start(self):
        self.client.post("/login", json={"username": "foo", "password": "bar"})

```

在上面的测试脚本中，我们定义了一个名为`WebsiteUser`的类，继承自`HttpUser`。该类包含了三个任务方法：`index_page`、`view_item`和`on_start`。其中，`index_page`用于访问首页，`view_item`用于访问商品详情页，`on_start`用于登录。

我们还定义了一个`wait_time`方法，用于指定每个用户任务之间的等待时间。在这个例子中，我们使用了一个随机等待时间，范围在5到9秒之间。

最后，在启动Locust时，我们可以通过命令行参数来指定并发用户数、每秒钟请求数、测试时间等参数。


当然需要关注内存和CPU的情况，因为它们也是系统性能的重要指标。在Locust性能测试中，可以使用Python编写测试脚本，通过监控系统的CPU和内存利用率，来了解系统的资源使用情况。同时，也可以设置阈值和警报机制，以便及时发现和解决性能问题。
在Locust测试中，可以使用Python的psutil库来监控系统的CPU和内存利用率。以下是一个示例代码：

```python
import psutil

# 获取CPU利用率
cpu = psutil.cpu_percent(interval=1)

# 获取内存利用率
memory = psutil.virtual_memory().percent
```

在测试过程中，可以定期获取系统的CPU和内存利用率，并记录下来。如果发现CPU或内存利用率过高，就需要分析测试结果，找出系统的瓶颈和问题，并进行优化。同时，也可以设置阈值和警报机制，当CPU或内存利用率超过一定阈值时，自动发送警报通知相关人员。