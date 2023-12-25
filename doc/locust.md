Locust是一款非常流行的Python负载测试工具，可以模拟大量用户访问和请求，支持多种协议和格式。以下是使用Locust针对项目后端做性能测试的步骤和关注的指标:

### 测试步骤

1. 安装Locust：使用pip命令安装Locust。

   ```
   pip install locust
   ```

2. 编写测试脚本：编写Locust测试脚本，用于模拟用户访问和请求。可以使用Python编写测试脚本，也可以使用YAML或JSON格式的配置文件。

3. 配置测试参数：配置测试参数，包括并发用户数、每秒钟请求数、测试时间等。

4. 启动Locust：启动Locust，并指定测试脚本和测试参数。

5. 分析测试结果：对测试结果进行分析，找出系统的瓶颈和问题。

### 关注的指标

1. 响应时间（Response Time）：响应时间指的是系统处理请求所需的时间，包括客户端发送请求、服务器处理请求和返回响应等所有时间。响应时间越短，表示系统响应速度越快。

2. 错误率（Error Rate）：错误率指的是请求失败的比例，包括HTTP错误、网络错误、服务器错误等。错误率越低，表示系统越稳定。

3. 吞吐量（Throughput）：吞吐量指的是系统在一定时间内处理的事务或请求的数量。通常以每秒钟处理的请求数（QPS）或每分钟处理的事务数（TPS）来衡量。吞吐量越高，表示系统处理能力越强。

### 测试脚本

以下是一个使用Locust编写的简单测试脚本，用于模拟用户访问一个Web应用程序。该脚本会启动100个并发用户，并在每秒钟发起10个请求。在测试过程中，会记录响应时间、错误率和吞吐量等指标。

```python
from locust import HttpUser, task, between

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
        self.client.post("/login", json={"username":"foo", "password":"bar"})

```

在上面的测试脚本中，我们定义了一个名为`WebsiteUser`的类，继承自`HttpUser`。该类包含了三个任务方法：`index_page`、`view_item`和`on_start`。其中，`index_page`用于访问首页，`view_item`用于访问商品详情页，`on_start`用于登录。

我们还定义了一个`wait_time`方法，用于指定每个用户任务之间的等待时间。在这个例子中，我们使用了一个随机等待时间，范围在5到9秒之间。

最后，在启动Locust时，我们可以通过命令行参数来指定并发用户数、每秒钟请求数、测试时间等参数。例如：

```
locust -f test.py --headless --users 100 --spawn-rate 10 --run-time 1m
```

这个命令会启动100个并发用户，并在每秒钟发起10个请求，持续运行1分钟。在测试过程中，Locust会记录响应时间、错误率和吞吐量等指标，并在Web界面上展示测试结果。



当然需要关注内存和CPU的情况，因为它们也是系统性能的重要指标。在Locust性能测试中，可以使用Python编写测试脚本，通过监控系统的CPU和内存利用率，来了解系统的资源使用情况。同时，也可以设置阈值和警报机制，以便及时发现和解决性能问题。
在Locust测试中，可以使用Python的psutil库来监控系统的CPU和内存利用率。以下是一个示例代码：

```python
import psutil

# 获取CPU利用率
cpu_percent = psutil.cpu_percent()

# 获取内存利用率
mem_percent = psutil.virtual_memory().percent
```

在测试过程中，可以定期获取系统的CPU和内存利用率，并记录下来。如果发现CPU或内存利用率过高，就需要分析测试结果，找出系统的瓶颈和问题，并进行优化。同时，也可以设置阈值和警报机制，当CPU或内存利用率超过一定阈值时，自动发送警报通知相关人员。