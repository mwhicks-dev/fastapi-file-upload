FROM python:3.10-bookworm

RUN mkdir -p /home/src
COPY . /home/src/

RUN pip install -r /home/src/requirements.txt
RUN pip install -r /home/src/test/requirements.txt

ENTRYPOINT pytest /home/src
