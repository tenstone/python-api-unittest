#!/usr/bin/python
# coding=utf-8

import logging
from logging.config import dictConfig
from config.base import LOGGING as logging_config
import sys
from functools import wraps


"""
返回logging对象
"""


def get_logger():
    dictConfig(logging_config)
    logger = logging.getLogger()
    return logger


"""
测试用例装饰器：打印日志
"""


def logger_for_test_case(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        testcase = func.__module__ + '.' + func.__name__
        get_logger().info('Running TestCase: ' + testcase)
        r = func(*args, **kwargs)
        r[0]['result']['testcase'] = testcase
        get_logger().info(dict(r[0]['result'], **r[1], **{"testcase": testcase}))
        get_logger().info('TestCase Finished.')
        return r
    return wrapper
