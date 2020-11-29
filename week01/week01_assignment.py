#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Describe :
# @Time     : 11/29/20 1:47 PM
# @Author   : Jinlei


import logging
import os
from datetime import datetime
from pathlib import Path


def logger_test(level='debug',
                fmt='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d %(message)s]'):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL,
    }

    now = datetime.strftime(datetime.today(), '%Y-%m-%d')
    log_name = f'/var/log/python-{now}'

    if not Path(log_name).exists():
        os.mkdir(log_name)

    logging.basicConfig(filename=log_name,
                        level=level_relations.get(level),
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format=fmt,
                        )
    logging.info('info message')


if __name__ == '__main__':
    logger_test()
