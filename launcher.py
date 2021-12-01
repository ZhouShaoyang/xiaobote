# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import time
import signal
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
browser = Browser()
browser.open(page.month_all)


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


def loop():
    snowboydecoder.play_audio_file()
    browser.open(page.detail)
    ais.record(audiofile=f'{os.getcwd()}/data/sound/order_deep1.pcm')
    order_deep1 = ais.sound2text(
        audiofile=f'{os.getcwd()}/data/sound/order_deep1.pcm')
    # 日期模块
    if aimod_date.check(order_deep1):
        ais.text2sound(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm',
                       text=aitime.get_date())
        browser.open(page.detail)
        ais.play(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm')
    # 星期模块
    elif aimod_week.check(order_deep1):
        ais.text2sound(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm',
                       text=aitime.get_week())
        browser.open(page.detail)
        ais.play(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm')
    # 时间模块
    elif aimod_time.check(order_deep1):
        ais.text2sound(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm',
                       text=aitime.get_time())
        browser.open(page.detail)
        ais.play(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm')
    # 天气模块
    elif aimod_weather.check(order_deep1):
        ais.text2sound(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm',
                       text=aiweather.get_weather())
        browser.open(page.month_all)
        ais.play(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm')
    # 日历模块
    elif aimod_cale_week.check(order_deep1):
        browser.open(page.detail)
    # 周历模块
    elif aimod_cale_week.check(order_deep1):
        browser.open(page.week_all)
    # 月历模块
    elif aimod_cale_month.check(order_deep1):
        browser.open(page.month_all)
    # 随笔模块
    elif aimod_essay.check(order_deep1):
        browser.open(page=page.essay_entry)
        time.sleep(5)
        browser.open(page=page.module_wait)
        time.sleep(5)
        browser.open(page=page.essay_result)
    # 海报模块
    elif aimod_poster.check(order_deep1):
        browser.open(page=page.post_entry)
        time.sleep(5)
        browser.open(page=page.module_wait)
        time.sleep(5)
        browser.open(page=page.post_result)
    # 分析师模块
    elif aimod_bv.check(order_deep1):
        browser.open(page=page.bv_entry)
        time.sleep(5)
        browser.open(page=page.module_wait)
        time.sleep(5)
        browser.open(page=page.bv_result)
    # 退出模块
    elif aimod_exit.check(order_deep1):
        browser.open(page.detail)
    # 重启模块
    elif aimod_reboot.check(order_deep1):
        os.system(command='sudo reboot')
    # 关机模块
    elif aimod_poweroff.check(order_deep1):
        os.system(command='sudo poweroff')
    # 异常重试模块
    else:
        ais.play(audiofile=f'{os.getcwd()}/data/sound/error.pcm')
        browser.open(page.month_all)


interrupted = False
model = f'{os.getcwd()}/data/model/wake-xiaolanxiaolan.umdl'
signal.signal(signal.SIGINT, signal_handler)
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)

if __name__ == '__main__':
    detector.start(detected_callback=loop,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)
    detector.terminate()
