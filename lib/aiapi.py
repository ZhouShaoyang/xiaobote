# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import requests
import traceback

from config import page

def api_essay(text):
    response = requests.get(f'{page.essay_api}{text}')
    try:
        aid = response.json()['data']['id']
        url = f'{page.essay_api_domain}{aid}'
        print(url)
        return url
    except Exception:
        print(traceback.format_exc())
        return None


if __name__ == "__main__":
    api_essay(text='达达利亚')
