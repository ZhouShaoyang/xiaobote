# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

from wake.examples.Python3 import snowboydecoder
import wave

# Demo code for detecting hotword in a .wav file
# Example Usage:
#  $ python demo3.py resources/snowboy.wav resources/models/snowboy.umdl
# Should print:
#  Hotword Detected!
#
#  $ python demo3.py resources/ding.wav resources/models/snowboy.umdl
# Should print:
#  Hotword Not Detected!

wave_file = f'{os.getcwd()}/data/sound/wake-xiaolanxiaolan.wav'
model_file = f'{os.getcwd()}/data/model/wake-xiaolanxiaolan.umdl'

f = wave.open(wave_file)
assert f.getnchannels() == 1, "Error: Snowboy only supports 1 channel of audio (mono, not stereo)"
assert f.getframerate() == 16000, "Error: Snowboy only supports 16K sampling rate"
assert f.getsampwidth() == 2, "Error: Snowboy only supports 16bit per sample"
data = f.readframes(f.getnframes())
f.close()

sensitivity = 0.5
detection = snowboydecoder.HotwordDetector(model_file, sensitivity=sensitivity)

ans = detection.detector.RunDetection(data)

if ans == 1:
    print('Hotword Detected!')
else:
    print('Hotword Not Detected!')

