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

from pypinyin import lazy_pinyin as py
from pypinyin.style._utils import get_initials
import itertools

sys.path.append(os.getcwd())

log = Logger()
ais = AiSound()

class DFAFilter(object):
    def __init__(self):
        self.keyword_chains = {}  # 关键词链表
        self.delimit = '\x00'  # 限定

    def add(self, keyword):
        keyword = keyword.lower()  # 关键词英文变为小写
        chars = keyword.strip()  # 关键字去除首尾空格和换行
        if not chars:  # 如果关键词为空直接返回
            return
        level = self.keyword_chains
        # 遍历关键字的每个字
        for i in range(len(chars)):
            # 如果这个字已经存在字符链的key中就进入其子字典
            if chars[i] in level:
                level = level[chars[i]]
            else:
                if not isinstance(level, dict):
                    break
                for j in range(i, len(chars)):
                    level[chars[j]] = {}
                    last_level, last_char = level, chars[j]
                    level = level[chars[j]]
                last_level[last_char] = {self.delimit: 0}
                break
        if i == len(chars) - 1:
            level[self.delimit] = 0

    def parse(self, path):
        with open(path, encoding='utf-8') as f:
            for keyword in f:
                self.add(str(keyword).strip())

    def filter(self, message, repl="*"):
        message = message.lower()
        ret = []
        start = 0
        while start < len(message):
            level = self.keyword_chains
            step_ins = 0
            for char in message[start:]:
                if char in level:
                    step_ins += 1
                    if self.delimit not in level[char]:
                        level = level[char]
                    else:
                        ret.append(message[start:start+step_ins])
                        start += step_ins - 1
                        break
                else:
                    break
            else:
                ret.append(message[start])
            start += 1
        return ret


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
dfa_zl = DFAFilter()
dfa_zl.parse(f"{os.getcwd}/data/keywords/calender.txt")

def dimTone(oriTone):
    # 模糊音
    sm = get_initials(oriTone, '_INITIALS_NOT_STRICT')
    ym = oriTone[len(sm):]
    d1, d2, d3 = ['zh', 'z'], ['ch', 'c'], ['sh', 's']
    d4, d5, d6 = ['n', 'l', 'r'], ['ang', 'an'], ['eng', 'en']
    d7, d8, d9 = ['ing', 'in'], ['f', 'h'], ['wang', 'huang']
    if oriTone in d9:
        return d9
    elif sm in d1:
        return [it + ym for it in d1]
    elif sm in d2:
        return [it + ym for it in d2]
    elif sm in d3:
        return [it + ym for it in d3]
    elif sm in d4:
        return [it + ym for it in d4]
    elif sm in d8:
        return [it + ym for it in d8]
    elif ym in d5:
        return [sm + it for it in d5]
    elif ym in d6:
        return [sm + it for it in d6]
    elif ym in d7:
        return [sm + it for it in d7]
    else:
        return [oriTone]

def check(recRes):
    # 如果命中返回True，反之False
    oriPy, final = py(recRes), []
    for it in oriPy:
        final.append(dimTone(it))
    final = itertools.product(*final)  # 星号不能忽略
    final = "".join([''.join(it) for it in final])
    if dfa_zl.filter(final):
        return True
    else:
        return False

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
    # 示例
    if check("周历"):
        browser.open(page.week_all)



interrupted = False
model = f'{os.getcwd()}/data/model/demo.umdl'
signal.signal(signal.SIGINT, signal_handler)
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)

if __name__ == '__main__':
    detector.start(detected_callback=loop,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)
    detector.terminate()
