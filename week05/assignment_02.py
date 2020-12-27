#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Describe :
# @Time     : 12/27/20 1:15 PM
# @Author   : Jinlei
import redis


def send_msg(content):
    print(f'短信消息已下发成功 {content}')


def send_sms(telephone_number: int, content):
    count = client.get(telephone_number)
    if not count:
        send_msg(content)
        client.set(telephone_number, 1)
    else:
        switch(count)(content, telephone_number)


def case1(content, telephone_number):
    send_msg(content)
    client.expire(telephone_number, 60)
    client.incr(telephone_number)


def case2(content, telephone_number):
    print('每分钟相同手机号最多发送五次,请稍后重试')


def case3(content, telephone_number):
    send_msg(content)
    client.incr(telephone_number)


def switch(x):
    return {
        '4': case1,
        '5': case2,
    }.get(x, case3)


if __name__ == '__main__':
    try:
        pool = redis.ConnectionPool(host='localhost', decode_responses=True)
        client = redis.Redis(connection_pool=pool)
    except Exception as e:
        print(e)

    send_sms(13800000000, 'hello')
    send_sms(13800000000, 'hello')
    send_sms(13800000000, 'hello')
    send_sms(13800000000, 'hello')
    send_sms(13800000000, 'hello')
    send_sms(13800000000, 'hello')
    send_sms(13800000000, 'hello')
    send_sms(13800000000, 'hello')
