FROM python:3.6

ADD container /container
RUN pip install -r /container/configs/pip-requirements.txt

WORKDIR /container
ENV PYTHONPATH '/container/'

EXPOSE 5000/tcp

CMD ["python" , "/container/configs/service.py"]