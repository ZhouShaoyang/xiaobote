# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import page


class Browser(object):
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--kiosk')
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.browser = webdriver.Chrome(options=self.options)

    def open(self, page):
        try:
            self.browser.get(url=page)
        except Exception as err:
            print(err)

    def quit(self):
        self.browser.quit()


browser = Browser()
browser.open('http://localhost:9527/')
browser.open(page.littleblueman)
time.sleep(0.3)
browser.open(page.listening)
time.sleep(5)
browser.quit()
