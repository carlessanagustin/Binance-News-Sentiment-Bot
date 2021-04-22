FROM python:3.9-buster as python3-debian-buster

COPY ./requirements.txt /
COPY ./*.py /
COPY ./*.csv /

RUN pip install -r /requirements.txt

ENV binance_api_url_testnet="https://testnet.binance.vision/api"
ENV binance_api_stalkbot_testnet="XXXX"
ENV binance_secret_stalkbot_testnet="XXXX"

ENTRYPOINT ["/usr/local/bin/python"]
CMD ["/news-analysis.py"]
