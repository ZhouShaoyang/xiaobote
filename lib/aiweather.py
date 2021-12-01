# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import requests


def get_weather():
    url = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
    response = requests.get(url=url).json().get('data')
    detail = response.get('forecast')[0]
    sun = detail.get('type')
    high = detail.get('high')
    if '-' in high:
        high = high.replace('℃', '').replace(' ', '').replace('-', '负')
    else:
        high = high.replace('℃', '').replace(' ', '')
    low = detail.get('low')
    if '-' in low:
        low = low.replace('℃', '').replace(' ', '').replace('-', '负')
    else:
        low = low.replace('℃', '').replace(' ', '')
    now = response.get('wendu')
    wind = detail.get('fengxiang')
    health = response.get('ganmao')
    text = f'今日天气，{sun}，最{high}度，最{low}度，当前{now}度，{wind}，{health}'
    print(text)
    return text


if __name__ == "__main__":
    get_weather()
