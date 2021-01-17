#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Describe :
# @Time     : 1/17/21 3:49 PM
# @Author   : Zhang JinLei


"""
    作业二：
        自定义一个 python 函数，实现 map() 函数的功能。
"""


def map_customize(fun_obj, *iterators):
    """
        customize high-order function map
    """
    try:
        i = 0
        while 1:
            yield fun_obj(*[j[i] for j in iterators])
            i += 1
    except IndexError:
        pass


if __name__ == "__main__":
    data_list = [1, 3, 5, 6]
    result = map_customize(lambda x, y: x + y, data_list, data_list)
    print(list(result))
