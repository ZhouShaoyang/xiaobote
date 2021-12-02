# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import re
import itertools
from pypinyin import lazy_pinyin as py
from pypinyin.style._utils import get_initials


class AiModule(object):
    """
    :Module: 日期,星期,时间,天气,日历,周历,月历,菜单,随笔,海报,分析师,退出,重启,关机
    """
    def __init__(self, module):
        self.module = module
        self.module_keywords_mapping = {
            '日期': ['日期', '几号'],
            '星期': ['星期', '周几'],
            '时间': ['时间', '报时', '几点'],
            '天气': ['天气', '天怎么样', '天咋样'],
            '日历': ['日历'],
            '周历': ['周历'],
            '月历': ['月历'],
            '菜单': ['目录', '菜单', '导航'],
            '随笔': ['随笔'],
            '海报': ['海报'],
            '分析师': ['分析师', '必威', 'bv', 'blueview'],
            '退出': ['关闭, 退出, 主页'],
            '重启': ['重启', '重置'],
            '关机': ['关机'],
            '示例-随笔-蓝标下一个十年': ['蓝标下一个十年'],
            '示例-随笔-倾听元宇宙时代': ['倾听元宇宙时代'],
            '示例-随笔-恰似而立之年': ['恰似而立之年']
        }

    def dimTone(self, oriTone):
        # 模糊音
        sm = get_initials(oriTone, '_INITIALS_NOT_STRICT')
        ym = oriTone[len(sm):]
        d1 = ['zh', 'z']  # 平舌卷舌不分
        d2 = ['ch', 'c']  # 平舌卷舌不分
        d3 = ['sh', 's']  # 平舌卷舌不分
        d4 = ['n', 'l']  # 鼻音边音不分
        d5 = ['ang', 'an']  # 前后鼻音不分
        d6 = ['eng', 'en']  # 前后鼻音不分
        d7 = ['ing', 'in']  # 前后鼻音不分
        d8 = ['f', 'h']  # 唇齿舌根不分
        if sm in d1:
            return [it + ym for it in d1]
        elif sm in d2:
            return [it + ym for it in d2]
        elif sm in d3:
            return [it + ym for it in d3]
        elif sm in d4:
            return [it + ym for it in d4]
        elif ym in d5:
            return [sm + it for it in d5]
        elif ym in d6:
            return [sm + it for it in d6]
        elif ym in d7:
            return [sm + it for it in d7]
        elif sm in d8:
            return [it + ym for it in d8]
        else:
            return [oriTone]

    def check(self, recRes):
        # 如果命中返回True，反之False
        oriPy, final = py(recRes), []
        for it in oriPy:
            final.append(self.dimTone(it))
        final = itertools.product(*final)  # 星号不能忽略
        final = ",".join([''.join(it) for it in final])
        for keywords in self.module_keywords_mapping.get(self.module):
            if re.search(str.lower(''.join(py(keywords))), str.lower(final)):
                return True
        return False


if __name__ == '__main__':
    mod = AiModule(module='日期')
    print(mod.check('今天几号了'))
    mod = AiModule(module='时间')
    print(mod.check('报时'))
    mod = AiModule(module='随笔')
    print(mod.check('水笔'))
    mod = AiModule(module='分析师')
    print(mod.check('BV分析师'))
