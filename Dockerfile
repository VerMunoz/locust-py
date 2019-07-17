FROM python:3.6.3-alpine3.6
RUN pip install requests

RUN mkdir /locust
WORKDIR /locust

COPY locust.py /locust 

#CMD python locust.py 

COPY docker-entrypoint.sh /
EXPOSE 8089
ENTRYPOINT ["/docker-entrypoint.sh"]
