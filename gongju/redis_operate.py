import redis
from config.setting import REDIS_HOST, REDIS_PORT, EXPIRE_TIME


class RedisDb:
    """启动redis服务:
    docker run -d --name my-redis -p 6379:6379 redis
    docker ps:
    CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                    NAMES
    ea11f1223a80   redis     "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:6379->6379/tcp   my-redis
    """

    def __init__(self, host, port):
        # 建立数据库连接
        self.r = redis.Redis(
            host=host,
            port=port,
            decode_responses=True,  # get() 得到字符串类型的数据
        )

    def handle_redis_token(self, key, value=None):
        if value:  # 如果value非空，那么就设置key和value，EXPIRE_TIME为过期时间
            self.r.set(key, value, ex=EXPIRE_TIME)
        else:  # 如果value为空，那么直接通过key从redis中取值
            redis_token = self.r.get(key)
            return redis_token


redis_db = RedisDb(REDIS_HOST, REDIS_PORT)
