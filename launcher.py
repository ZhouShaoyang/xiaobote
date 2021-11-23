# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from util.logger import Logger
from config import page

sys.path.append(os.getcwd())

log = Logger()


class Browser(object):
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--kiosk')
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.browser = webdriver.Chrome(options=self.options)

    def open(self, page):
        try:
            self.browser.get(url=page)
            log.info(message=f'open {page}')
        except Exception as err:
            log.error(message=f'ope {page} {err}')


if __name__ == '__main__':
    browser = Browser()
    browser.open(page.month_all)
    time.sleep(6)
    browser.open(page.month_opt)
    time.sleep(6)
    browser.open(page.essay_entry)
    time.sleep(3)
    browser.open(page.essay_result)
    time.sleep(6)
    browser.open(page.bv_entry)
    time.sleep(3)
    browser.open(page.bv_result)
    time.sleep(6)
    browser.open(page.post_entry)
    time.sleep(3)
    browser.open(page.post_result)
    time.sleep(6)
    browser.open(page.week_all)
