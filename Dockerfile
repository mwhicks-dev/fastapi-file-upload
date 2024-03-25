FROM python:3.10-bookworm

RUN mkdir -p /home/src
COPY src/ /home/src/

RUN pip install -r /home/src/requirements.txt

ENTRYPOINT python /home/src/main.py
