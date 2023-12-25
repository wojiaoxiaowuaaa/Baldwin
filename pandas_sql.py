#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine

# 创建一个MySQL数据库的连接对象 使用pymysql驱动的话会有警告信息 所以用create_engine.  mysql表示使用MySQL数据库 pymysql表示使用Python中的pymysql库作为数据库API 它是MySQL的一个Python接口 用于与MySQL数据库进行交互
conn = create_engine('mysql+pymysql://root:123456@localhost/mydatabase')

# 通过SQL从数据库读取数据创建DataFrame
df5 = pd.read_sql('select * from users', conn, index_col='user_id')
df5.to_csv('~/Desktop/test.csv')
print(df5)
