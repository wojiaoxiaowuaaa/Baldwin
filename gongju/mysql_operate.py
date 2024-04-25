import pymysql
from config.setting import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB


class MysqlDb:
    """部署docker MySQL并做容器端口映射
    docker ps
    ea7746dcbb9d   mysql:latest   "docker-entrypoint.s…"   13 days ago    Up 2 hours    0.0.0.0:3306->3306/tcp, 33060/tcp   mysql-wl
    """
    def __init__(self, host, port, user, passwd, db):
        # 建立数据库连接
        self.conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, autocommit=True)
        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):  # 析构方法，对象资源被释放时触发，在对象即将被删除时的最后操作. 用于在对象被销毁时释放资源.在这里,它关闭了游标 self.cur 和数据库连接 self.conn.
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data

    def execute_db(self, sql, data):
        """更新/新增/删除
        使用Demo 参数化查询(该写法可以避免SQL注入的风险):
        sql = " INSERT INTO test_result (platform, device_id, tc, task_id, result) VALUES (%s, %s, %s, %s, %s) "
        data = (platform, device_id, tc, task_id, result)
        db.execute_db(sql, data)
        """
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用 execute() 执行sql
            self.cur.execute(sql, data)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print("操作出现错误：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()


db = MysqlDb(MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB)

