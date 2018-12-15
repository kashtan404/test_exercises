FROM alpine:3.8

ADD requirements.txt /

RUN apk --no-cache update && apk --no-cache add python3
RUN pip3 install --no-cache-dir -r /requirements.txt && rm -rf /var/cache/apk/*

ADD helpers/*.py /helpers/
ADD getweather.py /

ENTRYPOINT ["/usr/bin/env", "python3", "/getweather.py"]
