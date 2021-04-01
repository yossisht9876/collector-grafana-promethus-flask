FROM python:3.6

ADD container /container
RUN pip install -r /container/pip-requirements.txt

WORKDIR /container
ENV PYTHONPATH '/container/'

EXPOSE 9000/tcp

CMD ["python" , "/container/collector.py"]