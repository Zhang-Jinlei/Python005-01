#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Describe :
# @Time     : 12/6/20 9:17 PM
# @Author   : Jinlei

# 使用 requests 库获取知乎任意一个话题下排名前 15 条的答案内容
# 知乎提问：请问第一门编程语言学python靠谱吗？

# TODO:我原本练习使用老师课上讲的「多线程」的方式来实现本次作业。老师课上提供的范例
#  有翻页的效果，而我在做作业的时候，遇到的问题是和翻页比较类似——需要滑动鼠标才会显示
#  更多的答案。不然的话抓取回来的答案一般只有几个，没有达到15个。因为今天赶在周末了，
#  所以先把基本的功能实现，后续再迭代代码。

# TODO:我简单搜索过如何解决「滑动鼠标显示更多答案」的这个问题，但今天貌似时间比较紧，
#  所以才有了这个TODO。


import requests
import json
from lxml import etree
from time import sleep


def get_answers(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    header = {'user-agent': user_agent}

    try:
        response = requests.get(url, headers=header)
        html = etree.HTML(response.text)
        answers = html.xpath('//div[@class="RichContent-inner"]/span')
        for answer in answers:
            try:
                answer_res = answer.xpath('./p/text()')
                response = {
                    'answer_res': answer_res,
                }
                with open('zhihu_answers.json', 'a', encoding='utf-8') as f:
                    json.dump(response, f, ensure_ascii=False)
            except Exception as e:
                print('answer error', e)

    except Exception as e:
        print('page error', e)


if __name__ == '__main__':
    url = f'https://www.zhihu.com/question/388547219'
    get_answers(url)

    sleep(5)
