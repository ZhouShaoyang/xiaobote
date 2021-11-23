# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import logging


class Logger(object):
    """
    :Description: 日志记录工具
    :Param None
    """
    def __init__(self):
        log_format = '[%(asctime)s] [%(levelname)s]\t%(message)s'
        logging.basicConfig(level=logging.INFO, format=log_format)

    def info(self, message):
        """
        :Description: INFO级别日志记录
        :Param message: 日志信息
        :Return: 记录完毕返回True
        """
        logging.info(message)

    def error(self, message):
        """
        :Description: ERROR级别日志记录
        :Param message: 日志信息
        :Return: 记录完毕返回True
        """
        logging.error(message)
