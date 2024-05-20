#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine

# 创建一个MySQL数据库的连接对象.使用pymysql驱动的话会有警告信息 所以用create_engine.mysql表示使用MySQL数据库 pymysql表示使用Python中的pymysql库作为数据库API 它是MySQL的一个Python接口 用于与MySQL数据库进行交互
engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root', '123456', 'localhost', '3306', 'flask_demo'))
# 这里注意升到较新的sqlalchemy版本
# create_engine 是 SQLAlchemy 提供的一个函数，用于创建一个数据库引擎对象，用于连接和与数据库进行交互。它的作用是根据指定的数据库连接---字符串（也称为数据库引擎 URL）来创建一个数据库引擎对象。
# conn = create_engine('mysql+pymysql://root:123456@localhost/flask_demo')

# 通过SQL从数据库读取数据创建DataFrame
df = pd.read_sql('select * from test_result', engine, index_col='id')

# df.to_csv('~/Desktop/test.csv')
print(df)


