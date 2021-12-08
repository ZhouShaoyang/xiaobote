# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import time
import signal
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from wake.examples.Python3 import snowboydecoder

from util.logger import Logger
from config import page
from lib import aitime
from lib import aiweather
from lib.aisound import AiSound
from lib.aimodule import AiModule

log = Logger()


class Browser(object):
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--kiosk')
        self.options.add_experimental_option('excludeSwitches',
                                             ['enable-automation'])
        self.browser = webdriver.Chrome(options=self.options)

    def open(self, page):
        try:
            self.browser.get(url=page)
            log.info(message=f'open {page}')
        except Exception as err:
            log.error(message=f'ope {page} {err}')


ais = AiSound()
aimod_date = AiModule(module='日期')
aimod_week = AiModule(module='星期')
aimod_time = AiModule(module='时间')
aimod_weather = AiModule(module='天气')
aimod_cale_day = AiModule(module='日历')
aimod_cale_week = AiModule(module='周历')
aimod_cale_month = AiModule(module='月历')
aimod_essay = AiModule(module='随笔')
aimod_poster = AiModule(module='海报')
aimod_bv = AiModule(module='分析师')
aimod_exit = AiModule(module='退出')
aimod_reboot = AiModule(module='重启')
aimod_poweroff = AiModule(module='关机')

aimod_demo_essay_lbxygsn = AiModule(module='示例-随笔-蓝标下一个十年')
aimod_demo_essay_qtyyzsd = AiModule(module='示例-随笔-倾听元宇宙时代')
aimod_demo_essay_qselzn = AiModule(module='示例-随笔-恰似而立之年')

browser = Browser()
browser.open('http://localhost:9527/')


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


def loop():
    # 播放识别音，打开听取页面
    snowboydecoder.play_audio_file()
    browser.open(page.littleblueman)
    browser.open(page.listening)
    # 记录听取内容
    ais.record(audiofile=f'{os.getcwd()}/data/sound/order_deep1.pcm',
               recordtime=5)
    order_deep1 = ais.sound2text(
        audiofile=f'{os.getcwd()}/data/sound/order_deep1.pcm')
    print(order_deep1)
    # 日期模块
    if aimod_date.check(order_deep1):
        ais.text2sound(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm',
                       text=aitime.get_date())
        browser.open(page.cale_month)
        ais.play(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm')
    # 星期模块
    elif aimod_week.check(order_deep1):
        ais.text2sound(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm',
                       text=aitime.get_week())
        browser.open(page.cale_month)
        ais.play(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm')
    # 时间模块
    elif aimod_time.check(order_deep1):
        ais.text2sound(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm',
                       text=aitime.get_time())
        browser.open(page.cale_month)
        ais.play(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm')
    # 天气模块
    elif aimod_weather.check(order_deep1):
        ais.text2sound(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm',
                       text=aiweather.get_weather())
        browser.open(page.cale_month)
        ais.play(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm')
    # 日历模块
    elif aimod_cale_day.check(order_deep1):
        browser.open(page.cale_day)
    # 周历模块
    elif aimod_cale_week.check(order_deep1):
        browser.open(page.cale_week)
    # 月历模块
    elif aimod_cale_month.check(order_deep1):
        browser.open(page.cale_month)
    # 随笔模块
    elif aimod_essay.check(order_deep1):
        browser.open(page.essay)
        ais.record(audiofile=f'{os.getcwd()}/data/sound/order_essay.pcm',
                   recordtime=8)
        browser.open(page.loading)
        order_essay = ais.sound2text(
            audiofile=f'{os.getcwd()}/data/sound/order_essay.pcm')
        if aimod_demo_essay_lbxygsn.check(order_essay):
            browser.open(page.demo_essay_lbxygsn)
        elif aimod_demo_essay_qtyyzsd.check(order_essay):
            browser.open(page.demo_essay_qtyyzsd)
        elif aimod_demo_essay_qselzn.check(order_essay):
            browser.open(page.demo_essay_qselzn)
        else:
            requests.get(page.essay_api)
            browser.open(page.essay_result)
    # 海报模块
    elif aimod_poster.check(order_deep1):
        browser.open(page.poster)
        ais.record(audiofile=f'{os.getcwd()}/data/sound/order_poster.pcm',
                   recordtime=8)
        browser.open(page.loading)
        requests.get(page.poster_api)
        browser.open(page.poster_result)
    # 分析师模块
    elif aimod_bv.check(order_deep1):
        browser.open(page.bv)
    # 退出模块
    elif aimod_exit.check(order_deep1):
        browser.open(page.cale_month)
    # 重启模块
    elif aimod_reboot.check(order_deep1):
        os.system(command='sudo reboot')
    # 关机模块
    elif aimod_poweroff.check(order_deep1):
        os.system(command='sudo poweroff')
    # 异常重试模块
    else:
        ais.play(audiofile=f'{os.getcwd()}/data/sound/error.pcm')
        browser.open(page.cale_month)


interrupted = False
model = f'{os.getcwd()}/data/model/wake-xiaolanxiaolan-honglei.umdl'
signal.signal(signal.SIGINT, signal_handler)
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)

if __name__ == '__main__':
    detector.start(detected_callback=loop,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)
    detector.terminate()
