FROM python:3.7

WORKDIR /app

ADD kconsumer.py /app/kconsumer.py
ADD kproducer.py /app/kproducer.py

RUN pip install -i https://mirrors.ustc.edu.cn/pypi/web/simple/ kafka-python
RUN python kconsumer.py

CMD ["python", "kproducer.py"]

