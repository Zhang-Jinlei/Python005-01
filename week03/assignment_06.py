#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Describe :
# @Time     : 12/13/20 11:02 PM
# @Author   : Jinlei


# TODO:时间有点来不及了，先把三张表基本创建出来（字段设计未优化）

import pymysql
from sqlalchemy import Table, Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from dbconfig import read_db_config
import sys

Base = declarative_base()


# 定义用户表
class User_table(Base):
    __tablename__ = 'user_orm'
    id = Column(Integer(), primary_key=True)
    name = Column(String(50), index=True, nullable=False)


# 定义资产表
class Asset_table(Base):
    __tablename__ = 'asset_orm'
    asset_id = Column(Float(), index=True, nullable=False)
    user_id = Column(Integer(), primary_key=True, index=True, nullable=False)
    balance = Column(Float(), index=True, nullable=False)


# 定义交易审计表
class Transaction_table(Base):
    __tablename__ = 'trx_orm'
    trx_id = Column(Integer(), primary_key=True)
    from_id = Column(Integer(), index=True, nullable=False)
    to_id = Column(Integer(), index=True, nullable=False)
    amount = Column(Float(), index=True, nullable=False)
    create_on = Column(DateTime(), index=True, default=datetime.now)
