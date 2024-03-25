FROM python:3.10-bookworm

COPY . /home

RUN pip install -r /home/src/requirements.txt

ENTRYPOINT python /home/main.py
