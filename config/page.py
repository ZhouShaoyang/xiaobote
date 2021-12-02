# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

mode = 'FAKE'

if mode == 'FAKE':
    # 本地假链接
    cale_day = 'file:///home/pi/xiaobote/html/fake/cale_day.html'
    cale_week = 'file:///home/pi/xiaobote/html/fake/cale_week.html'
    cale_month = 'file:///home/pi/xiaobote/html/fake/cale_month.html'
    cale_month_day = 'file:///home/pi/xiaobote/html/fake/cale_month_day.html'
    cale_month_opt = 'file:///home/pi/xiaobote/html/fake/cale_month_opt.html'

    listening = 'file:///home/pi/xiaobote/html/fake/listening.html'
    loading = 'file:///home/pi/xiaobote/html/fake/loading.html'

    bv = 'file:///home/pi/xiaobote/html/fake/bv.html'
    bv_result = 'file:///home/pi/xiaobote/html/fake/bv_result.html'
    poster = 'file:///home/pi/xiaobote/html/fake/poster.html'
    poster_result = 'file:///home/pi/xiaobote/html/fake/poster_result.html'
    essay = 'file:///home/pi/xiaobote/html/fake/essay.html'
    essay_result = 'file:///home/pi/xiaobote/html/fake/essay_result.html'

    demo_essay_lbxygsn = 'http://essays.xiaobote.com/#/article?&id=61a07d58899e0114e9cb4b44'
    demo_essay_qtyyzsd = 'http://essays.xiaobote.com/#/article?id=61a07c8b899e0114e9cb4b41'
    demo_essay_qselzn = 'http://essays.xiaobote.com/#/article?id=61a07ce4899e0114e9cb4b42'

    essay_api = 'http://www.baidu.com'
    poster_api = 'http://www.baidu.com'

else:
    # 联网真实链接
    cale_day = 'file:///home/pi/xiaobote/html/fake/cale_day.html'
    cale_week = 'file:///home/pi/xiaobote/html/fake/cale_week.html'
    cale_month = 'file:///home/pi/xiaobote/html/fake/cale_month.html'
    cale_month_day = 'file:///home/pi/xiaobote/html/fake/cale_month_day.html'
    cale_month_opt = 'file:///home/pi/xiaobote/html/fake/cale_month_opt.html'

    listening = 'file:///home/pi/xiaobote/html/fake/listening.html'
    loading = 'file:///home/pi/xiaobote/html/fake/loading.html'

    bv = 'file:///home/pi/xiaobote/html/fake/bv.html'
    bv_result = 'file:///home/pi/xiaobote/html/fake/bv_result.html'
    poster = 'file:///home/pi/xiaobote/html/fake/poster.html'
    poster_result = 'file:///home/pi/xiaobote/html/fake/poster_result.html'
    essay = 'file:///home/pi/xiaobote/html/fake/essay.html'
    essay_result = 'file:///home/pi/xiaobote/html/fake/essay_result.html'

    demo_essay_lbxygsn = 'http://essays.xiaobote.com/#/article?title=%E8%93%9D%E6%A0%87%E4%B8%8B%E4%B8%80%E4%B8%AA%E5%8D%81%E5%B9%B4&id=61a07d58899e0114e9cb4b44'
    demo_essay_qtyyzsd = 'http://essays.xiaobote.com/#/article?title=%E5%80%BE%E5%90%AC%E5%85%83%E5%AE%87%E5%AE%99%E6%97%B6%E4%BB%A3&id=61a07c8b899e0114e9cb4b41'
    demo_essay_qselzn = 'http://essays.xiaobote.com/#/article?title=%E6%81%B0%E4%BC%BC%E8%80%8C%E7%AB%8B%E4%B9%8B%E5%B9%B4&id=61a07ce4899e0114e9cb4b42'

    essay_api = 'http://www.baidu.com'
    poster_api = 'http://www.baidu.com'
