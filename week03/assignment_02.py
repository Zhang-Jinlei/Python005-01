#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Describe :
# @Time     : 12/13/20 9:58 PM
# @Author   : Jinlei


import pymysql
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# 用ORM创建表格
Base = declarative_base()


class UserTable(Base):
    __tablename__ = 'assignment_02_orm'
    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    age = Column(SmallInteger())
    birthday = Column(Date())
    gender = Column(String(5))
    education = Column(String(20))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)

    def __repr__(self):
        return "UserTable(id='{self.id}', " \
               "name={self.name})".format(self=self)


dburl = "mysql+pymysql://testuser:testpass@127.0.0.1:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding='utf-8')
Base.metadata.create_all(engine)

# 用 pymysql 插入三条数据
db = pymysql.connect("127.0.0.1", "testuser", "testpass", "testdb")
try:
    sql = '''INSERT INTO assignment_02_orm (name, age, birthday, gender, education, created_on, updated_on) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
    values = (
        ('David Zhang', 42, '1990-1-12', 'M',
         'Bachelor', datetime.now(), datetime.now()),
        ('Ting Zhi', 30, '1993-10-24', 'F',
         'Master', datetime.now(), datetime.now()),
        ('Ella Wang', 20, '2000-08-24', 'M',
         'High School', datetime.now(), datetime.now())
    )
    with db.cursor() as cursor:
        cursor.executemany(sql, values)
    db.commit()
except Exception as e:
    print(f'Insert error: {e}')

# 用pymysql查询所有的数据
try:
    sql = '''SELECT name, age, birthday, gender, education FROM assignment_02_orm'''
    with db.cursor() as cursor:
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            print(result)
    db.commit()
except Exception as e:
    print(f'SELECT error: {e}')
finally:
    db.close()
