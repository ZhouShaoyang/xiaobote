# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from util.logger import Logger

log = Logger()


class Browser(object):
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--kiosk')
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.browser = webdriver.Chrome(options=self.options)

    def open(self, page, module):
        try:
            self.browser.get(url=page)
            log.info(message=f'open {module} {page}')
        except Exception as err:
            log.error(message=f'open {module} {page} {err}')


if __name__ == '__main__':
    options = Options()

    browser = webdriver.Chrome(options=options)
    browser.get('file:///home/pi/xiaobote/html/fake.html')
