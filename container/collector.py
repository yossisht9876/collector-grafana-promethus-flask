from prometheus_client import start_http_server, Summary, Counter, Histogram
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily, Summary, Info, Enum, Gauge


import random
import requests
import urllib.request
import time
#from bs4 import BeautifulSoup

from prometheus_client import Histogram
import urllib.request



g = Gauge('Request_duration', 'Description of gauge')
g1 = Gauge('status_code', 'Description of gauge')
#i = Info('Content_Type', 'Description of info')
#g2 = Gauge('content_type', 'Description of gauge')


# Decorate function with metric.

def process_request(t):
    url = 'https://www.armis.com/'
    response = requests.get(url)
    print(urllib.request.urlopen("https://www.armis.com/").getcode())
    print(response.elapsed.total_seconds())

    h = requests.head(url)
    header = h.headers
    content_type = response.headers['content-type']
    print (content_type)

    print (response)

    g.set(response.elapsed.total_seconds())
    g1.set(urllib.request.urlopen("https://www.armis.com/").getcode())
    #g2.set(content_type())
    #i.info(content_type())
    #i.info(response)

    time.sleep(30)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9000)
    # Generate some requests.
    while True:
        process_request(random.random())