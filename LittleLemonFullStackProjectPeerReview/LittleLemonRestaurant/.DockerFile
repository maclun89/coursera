FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN mkdir /LittleLemon
WORKDIR /LittleLemon
ADD requirements.txt /LittleLemon/
RUN pip install -r requirements.txt
ADD . /LittleLemon/