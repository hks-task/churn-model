FROM continuumio/miniconda3:4.5.12

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD pip-requirements.txt pip-requirements.txt
RUN pip install -r pip-requirements.txt

ADD . .

ENTRYPOINT ["python", "-u", "main.py"]