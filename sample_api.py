# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import requests
from config import page

response = requests.get(page.essay_api + '测试用例').json()
did = response.get('data').get('id')
print(page.essay_api_domain + did)
