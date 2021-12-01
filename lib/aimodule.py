# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

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
            '分析师': ['分析师', 'BV', '必威'],
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
        if DFAFilter(self.module_keywords_mapping.get(self.module)).filter(final):
            return True
        else:
            return False


class DFAFilter(object):
    def __init__(self, keywords):
        self.keyword_chains = {}  # 关键词链表
        self.delimit = '\x00'  # 限定
        self.keywords = keywords

        def add(keyword):
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

        [add(''.join(py(x))) for x in self.keywords]

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
                        ret.append(message[start:start + step_ins])
                        start += step_ins - 1
                        break
                else:
                    break
            else:
                ret.append(message[start])
            start += 1
        return ret


if __name__ == '__main__':
    mod = AiModule(module='日期')
    print(mod.check('今天几号了'))
    mod = AiModule(module='时间')
    print(mod.check('报时'))
    mod = AiModule(module='随笔')
    print(mod.check('水笔'))
    pass
