# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

mode = 'REAL'
web = 'OFFLINE'

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

elif mode == 'REAL':
    domain = 'http://127.0.0.1:9527/#/'
    cale_day = f'{domain}Details'
    cale_week = f'{domain}Week'
    cale_month = f'{domain}'
    cale_month_day = f'{domain}'
    cale_month_opt = f'{domain}'

    littleblueman = f'{domain}LittleBlueMan'
    listening = f'{domain}Awaken'
    loading = f'{domain}Loaded'

    bv = 'https://appvhc2xld68325.h5.xiaoeknow.com/'
    poster = f'{domain}PosterLoad'
    poster_result = f'{domain}Poster'
    essay = f'{domain}InformalEssayLoad'
    essay_result = f'{domain}InformalEssay'

    demo_essay_lbxygsn = 'http://essays.xiaobote.com/#/article?id=61a07d58899e0114e9cb4b44'
    demo_essay_qtyyzsd = 'http://essays.xiaobote.com/#/article?id=61a07c8b899e0114e9cb4b41'
    demo_essay_qselzn = 'http://essays.xiaobote.com/#/article?id=61a07ce4899e0114e9cb4b42'

    essay_api = 'http://xiaobot.automc.cn/api/intelligent/write/article/loudspeaker/box/create?title='
    essay_api_domain = 'http://essays.automc.cn/#/article?id='
    poster_api = 'http://xiaobot.automc.cn/api/intelligent/write/article/loudspeaker/box/create?title='
    poster_api_domain = 'http://essays.automc.cn/#/article?id='

else:
    print('网页模式错误，需要选择FAKE数据或REAL数据。')
