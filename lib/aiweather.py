# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import requests

from config import page

if page.web == 'OFFLINE':
    def get_weather():
        text = '今日天气，多云，最高温10度，最低温负3度，当前3度，西北风，感冒高发期，尽量避免外出，外出戴口罩防护。'
        print(text)
        return text
else:
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
