FROM ubuntu:16.04

RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
    && sed -i s@/ports.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
    && apt update \
    && apt -y install wget unzip build-essential portaudio19-dev python python-dev python-pip python-scipy python-pyaudio

RUN cd root/ \
    && wget https://github.com/seasalt-ai/snowboy/archive/master.zip && unzip master.zip \
    && cd snowboy-master/examples/Python/ \

CMD python generate_pmdl.py -r1=model/record1.wav -r2=model/record2.wav -r3=model/record3.wav -lang=en -n=model/hotword.pmdl
