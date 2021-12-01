FROM ubuntu:16.04

RUN sed -i s@/ports.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \ 
    && apt update \
    && apt -y install wget unzip build-essential python python-dev python-pip portaudio19-dev

RUN cd root/ \
    && wget https://github.com/seasalt-ai/snowboy/archive/master.zip && unzip master.zip \
    && cd snowboy-master \
    && cd examples/Python \
    && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD cd snowboy-master/ && \
    . venv/snowboy/bin/activate && \
    cd examples/Python && \
    python generate_pmdl.py -r1=model/record1.wav -r2=model/record2.wav -r3=model/record3.wav -lang=en -n=model/hotword.pmdl
