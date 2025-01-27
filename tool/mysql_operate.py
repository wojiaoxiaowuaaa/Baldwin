import pymysql
from config.setting import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB


class MysqlDb:
    def __init__(self, host, port, user, passwd, db_name):
        # 建立数据库连接
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=passwd,
            database=db_name,
            autocommit=True,
        )
        # 通过 cursor() 创建游标对象,并让查询结果以字典格式输出
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        # 析构方法,对象资源被释放时触发,用于在对象被销毁时释放资源.在对象被垃圾回收时自动调用.在这里,它关闭了游标 self.cur 和数据库连接 self.conn.
        # 当对象的引用计数降为零时,Python 的垃圾回收机制会自动调用 __del__ 方法.
        self.cur.close()
        self.conn.close()

    def select_db(self, sql, params=None):
        # 参数化查询.params:可选参数,默认值为None,用于传递给SQL查询的参数.这在执行需要外部输入的参数化查询时非常重要,以防止SQL注入攻击.
        self.conn.ping(reconnect=True)
        # 当sql参数为SHOW DATABASES这样的无参数指令时,params参数为None或未被使用,不会影响整体的数据查询.因为这个SQL语句不需要外部参数,所以不会发生参数绑定,直接执行原生SQL命令.
        self.cur.execute(sql, params)
        # 返回一个包含查询结果中所有行的列表(列表的子元素为元祖tuple或字典dic)
        return self.cur.fetchall()

    def execute_db(self, sql, params=None):
        """参数化 防止SQL注入"""
        try:
            # 检查连接是否断开,如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用 execute() 执行sql
            self.cur.execute(sql, params)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print("操作出现错误:{}".format(e))
            # 回滚所有更改
            self.conn.rollback()


db = MysqlDb(MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB)

if __name__ == "__main__":
    data = db.select_db("select * from movies")
    print(data)
    # for _ in data: print(_)

    # data = """
    #     CREATE TABLE IF NOT EXISTS movies (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     movie_name VARCHAR(255) NOT NULL,
    #     movie_ VARCHAR(255)  NOT NULL,
    #     img_url VARCHAR(255) NOT NULL
    #     );
    #     """
    # db.execute_db(data)
