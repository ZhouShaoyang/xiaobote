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

sys.path.append(os.getcwd())

log = Logger()
ais = AiSound()


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
    browser.open(page.month_wait)
    ais.record(audiofile=f'{os.getcwd()}/data/sound/order_deep1.pcm')
    order_deep1 = ais.sound2text(
        audiofile=f'{os.getcwd()}/data/sound/order_deep1.pcm')
    if '报日期' in order_deep1:
        ais.text2sound(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm',
                       text=aitime.get_date())
        browser.open(page.month_all)
        ais.play(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm')
    elif '报星期' in order_deep1:
        ais.text2sound(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm',
                       text=aitime.get_week())
        browser.open(page.month_all)
        ais.play(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm')
    elif '报时间' in order_deep1:
        ais.text2sound(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm',
                       text=aitime.get_time())
        browser.open(page.month_all)
        ais.play(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm')
    elif '报天气' in order_deep1:
        ais.text2sound(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm',
                       text=aiweather.get_weather())
        browser.open(page.month_all)
        ais.play(audiofile=f'{os.getcwd()}/data/sound/exec_deep1.pcm')
    elif '打开随笔' in order_deep1 or '打开水笔' in order_deep1:
        browser.open(page=page.essay_entry)
        time.sleep(5)
        browser.open(page=page.module_wait)
        time.sleep(5)
        browser.open(page=page.essay_result)
    elif '打开海报' in order_deep1:
        browser.open(page=page.post_entry)
        time.sleep(5)
        browser.open(page=page.module_wait)
        time.sleep(5)
        browser.open(page=page.post_result)
    elif '打开分析师' in order_deep1:
        browser.open(page=page.bv_entry)
        time.sleep(5)
        browser.open(page=page.module_wait)
        time.sleep(5)
        browser.open(page=page.bv_result)
    elif '打开周历' in order_deep1 or '打开周丽' in order_deep1:
        browser.open(page.week_all)
    elif '回到主页' in order_deep1:
        browser.open(page.month_all)
    elif '关机' in order_deep1:
        os.system(command='sudo poweroff')
    elif '重启' in order_deep1:
        os.system(command='sudo reboot')
    else:
        ais.play(audiofile=f'{os.getcwd()}/data/sound/error.pcm')
        browser.open(page.month_all)


interrupted = False
model = f'{os.getcwd()}/data/model/demo.umdl'
signal.signal(signal.SIGINT, signal_handler)
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)

if __name__ == '__main__':
    detector.start(detected_callback=loop,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)
    detector.terminate()
