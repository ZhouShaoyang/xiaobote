# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import time
import ssl
import websocket
import pyaudio
import wave
import time
from util import iat
from util import tts


class AiSound(object):
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
        print(ws.result)
        return ws.result

    def text2sound(self, audiofile, text):
        wsParam = tts.Ws_Param(APPID=self.AppId, APISecret=self.APISecret, APIKey=self.APIKey, AudioFile=audiofile, Text=text)
        ws = tts.WS(wsParam=wsParam)
        websocket.enableTrace(False)
        wsUrl = wsParam.create_url()
        websock = websocket.WebSocketApp(wsUrl, on_message=ws.on_message, on_error=ws.on_error, on_close=ws.on_close)
        websock.on_open = ws.on_open
        websock.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
        return True

    def record(self, audiofile, recordtime):
        player = pyaudio.PyAudio()
        stream = player.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
        frames = []
        for r in range(0, int(16000 / 1024 * recordtime)):
            data = stream.read(1024)
            frames.append(data)
        stream.stop_stream()
        stream.stop_stream()
        stream.close()
        player.terminate()
        wf = wave.open(audiofile, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        wf.writeframes(b''.join(frames))
        wf.close()
        return True

    def play(self, audiofile):
        player = pyaudio.PyAudio()
        stream = player.open(format=player.get_format_from_width(2), channels=1, rate=16000, output=True)
        with open(audiofile, 'rb') as f:
            stream.write(f.read())
        time.sleep(0.3)
        stream.stop_stream()
        stream.close()
        player.terminate()
        return True


if __name__ == "__main__":
    ais = AiSound()
    ais.sound2text(audiofile=f'{os.getcwd()}/data/sound/demo_iat.pcm')
    ais.text2sound(audiofile=f'{os.getcwd()}/data/sound/demo_tts.pcm', text='这是1个文本转语音示例。')
    ais.play(audiofile=f'{os.getcwd()}/data/sound/demo_tts.pcm')
    ais.record(audiofile=f'{os.getcwd()}/data/sound/demo_record.pcm', recordtime=2)
    ais.play(audiofile=f'{os.getcwd()}/data/sound/demo_record.pcm')
    ais.sound2text(audiofile=f'{os.getcwd()}/data/sound/demo_record.pcm')

    ais.record(audiofile=f'{os.getcwd()}/data/sound/demo_海报.pcm', recordtime=2)
    ais.play(audiofile=f'{os.getcwd()}/data/sound/demo_海报.pcm')
    ais.sound2text(audiofile=f'{os.getcwd()}/data/sound/demo_海报.pcm')

    ais.record(audiofile=f'{os.getcwd()}/data/sound/demo_周历.pcm', recordtime=2)
    ais.play(audiofile=f'{os.getcwd()}/data/sound/demo_周历.pcm')
    ais.sound2text(audiofile=f'{os.getcwd()}/data/sound/demo_周历.pcm')

    ais.record(audiofile=f'{os.getcwd()}/data/sound/demo_随笔.pcm', recordtime=2)
    ais.play(audiofile=f'{os.getcwd()}/data/sound/demo_随笔.pcm')
    ais.sound2text(audiofile=f'{os.getcwd()}/data/sound/demo_随笔.pcm')
