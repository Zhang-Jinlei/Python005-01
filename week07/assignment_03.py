#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Describe :
# @Time     : 1/17/21 3:49 PM
# @Author   : Zhang JinLei


"""
    作业三：
        实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
"""

import datetime
from functools import wraps


def timer(func):
    @wraps(func)
    def out(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(f'function {func.__name__} '
              # f'cost {(end_time - start_time).seconds} seconds')
              f'cost {(end_time - start_time).microseconds} microseconds')
        return result

    return out


@timer
def add(x, y):
    return x + y


@timer
def package_position(*args):
    s = 0
    for i in args:
        s += i
    return s


@timer
def package_keyword(**kwargs):
    kwargs_reverse = dict()
    for i, j in kwargs.items():
        kwargs_reverse[j] = i
    return kwargs_reverse


add(1, 2)
package_position(5, 6, 7, 1, 2, 3)
package_keyword(m=2, n=1, c=11)
