# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import ssl
import websocket
from util import iat
from util import tts


class Sound(object):
    def __init__(self):
        self.AppId = 'a28fc810'
        self.APISecret = 'YWJkMDlmZmFlMDIxY2Y0ODE5MGJiMjAw'
        self.APIKey = 'a7c4a7ff3a585b31d60f5ded99526354'

    def sound2text(self, audiofile):
        wsParam = iat.Ws_Param(APPID=self.AppId, APISecret=self.APISecret, APIKey=self.APIKey, AudioFile=audiofile)
        ws = iat.WS(wsParam=wsParam)
        websocket.enableTrace(False)
        wsUrl = wsParam.create_url()
        websock = websocket.WebSocketApp(wsUrl, on_message=ws.on_message, on_error=ws.on_error, on_close=ws.on_close)
        websock.on_open = ws.on_open
        websock.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def text2sound(self, audiofile, text):
        wsParam = tts.Ws_Param(APPID=self.AppId, APISecret=self.APISecret, APIKey=self.APIKey, AudioFile=audiofile, Text=text)
        ws = tts.WS(wsParam=wsParam)
        websocket.enableTrace(False)
        wsUrl = wsParam.create_url()
        websock = websocket.WebSocketApp(wsUrl, on_message=ws.on_message, on_error=ws.on_error, on_close=ws.on_close)
        websock.on_open = ws.on_open
        websock.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


if __name__ == "__main__":
    s = Sound()
    s.sound2text(audiofile=f'{os.getcwd()}/data/sound/demo_iat.pcm')
    s.text2sound(audiofile=f'{os.getcwd()}/data/sound/demo_tts.pcm', text='这是1个文本转语音示例。')
