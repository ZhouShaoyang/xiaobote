# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import time


def get_date():
    text = time.strftime('今天是%Y年%m月%d号', time.localtime())
    print(text)
    return text


def get_week():
    text = time.strftime('本周是全年第%W周', time.localtime())
    print(text)
    return text


def get_time():
    text = time.strftime('当前时间是%H时%M分', time.localtime())
    print(text)
    return text


if __name__ == "__main__":
    get_date()
    get_week()
    get_time()
