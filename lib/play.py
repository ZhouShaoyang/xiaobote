# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import time
import pyaudio


def run(audiofile):
    player = pyaudio.PyAudio()
    stream = player.open(format=player.get_format_from_width(2),
                         channels=1,
                         rate=16000,
                         output=True)
    with open(audiofile, 'rb') as f:
        stream.write(f.read())
    time.sleep(0.3)
    stream.stop_stream()
    stream.close()
    player.terminate()
    return True


if __name__ == "__main__":
    run(audiofile=f'{os.getcwd()}/data/sound/demo_tts_s.pcm')
